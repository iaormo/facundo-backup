#!/usr/bin/env python3
"""
Fullstack Mastery - Phase 3: DevOps & System Design
CI/CD, Docker, Kubernetes, Cloud, Microservices
"""

import asyncio
import json
from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict, Any, Optional
from enum import Enum


# ============== CI/CD Pipeline ==============

class PipelineStage(Enum):
    BUILD = "build"
    TEST = "test"
    SECURITY = "security"
    DEPLOY = "deploy"


@dataclass
class PipelineJob:
    name: str
    stage: PipelineStage
    script: List[str]
    artifacts: List[str] = None
    dependencies: List[str] = None
    only: List[str] = None  # Branch names


class CICDPipeline:
    """CI/CD Pipeline configuration."""
    
    # GitHub Actions Example
    GITHUB_ACTIONS = """
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Lint
        run: npm run lint
      
      - name: Build
        run: npm run build
      
      - name: Upload build artifacts
        uses: actions/upload-artifact@v3
        with:
          name: build-files
          path: dist/

  test:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run unit tests
        run: npm run test:unit
      
      - name: Run integration tests
        run: npm run test:integration
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3

  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Run security audit
        run: npm audit --audit-level=moderate
      
      - name: Run Snyk security scan
        uses: snyk/actions/node@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}

  deploy-staging:
    needs: [build, test, security]
    if: github.ref == 'refs/heads/develop'
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to staging
        run: |
          echo "Deploying to staging environment"
          # Deployment commands here

  deploy-production:
    needs: [build, test, security]
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment: production
    steps:
      - name: Deploy to production
        run: |
          echo "Deploying to production environment"
          # Deployment commands here
"""


# ============== Docker ==============

DOCKERFILE_PRODUCTION = """
# Multi-stage build for production optimization
FROM node:18-alpine AS builder

WORKDIR /app

# Copy package files
COPY package*.json ./
RUN npm ci --only=production

# Copy source code
COPY . .

# Build application
RUN npm run build

# Production stage
FROM node:18-alpine AS production

# Security: Run as non-root user
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001

WORKDIR /app

# Copy built assets from builder
COPY --from=builder --chown=nextjs:nodejs /app/dist ./dist
COPY --from=builder --chown=nextjs:nodejs /app/node_modules ./node_modules
COPY --from=builder --chown=nextjs:nodejs /app/package.json ./package.json

# Set environment
ENV NODE_ENV=production
ENV PORT=3000

# Switch to non-root user
USER nextjs

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \\
  CMD node healthcheck.js || exit 1

# Start application
CMD ["node", "dist/server.js"]
"""

DOCKER_COMPOSE = """
version: '3.8'

services:
  # Application
  app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - DATABASE_URL=postgresql://postgres:password@db:5432/app
      - REDIS_URL=redis://redis:6379
      - JWT_SECRET=${JWT_SECRET}
    depends_on:
      - db
      - redis
    networks:
      - app-network
    restart: unless-stopped
    deploy:
      replicas: 2
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M

  # Database
  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=${DB_PASSWORD}
      - POSTGRES_DB=app
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    networks:
      - app-network
    restart: unless-stopped

  # Redis Cache
  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data
    networks:
      - app-network
    restart: unless-stopped

  # Nginx Reverse Proxy
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./ssl:/etc/nginx/ssl:ro
    depends_on:
      - app
    networks:
      - app-network
    restart: unless-stopped

volumes:
  postgres_data:
  redis_data:

networks:
  app-network:
    driver: bridge
"""


# ============== Kubernetes ==============

KUBERNETES_DEPLOYMENT = """
apiVersion: apps/v1
kind: Deployment
metadata:
  name: scaleplus-app
  namespace: production
  labels:
    app: scaleplus
    tier: backend
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: scaleplus
      tier: backend
  template:
    metadata:
      labels:
        app: scaleplus
        tier: backend
    spec:
      containers:
      - name: app
        image: scaleplus/app:latest
        ports:
        - containerPort: 3000
        env:
        - name: NODE_ENV
          value: "production"
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: db-credentials
              key: url
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 3000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 3000
          initialDelaySeconds: 5
          periodSeconds: 5
        securityContext:
          runAsNonRoot: true
          runAsUser: 1001
          readOnlyRootFilesystem: true
          allowPrivilegeEscalation: false
---
apiVersion: v1
kind: Service
metadata:
  name: scaleplus-service
  namespace: production
spec:
  selector:
    app: scaleplus
    tier: backend
  ports:
  - protocol: TCP
    port: 80
    targetPort: 3000
  type: ClusterIP
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: scaleplus-ingress
  namespace: production
  annotations:
    kubernetes.io/ingress.class: nginx
    cert-manager.io/cluster-issuer: letsencrypt-prod
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
    nginx.ingress.kubernetes.io/rate-limit: "100"
spec:
  tls:
  - hosts:
    - api.scaleplus.io
    secretName: scaleplus-tls
  rules:
  - host: api.scaleplus.io
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: scaleplus-service
            port:
              number: 80
"""


# ============== Cloud Architecture (AWS) ==============

AWS_ARCHITECTURE = """
# AWS CloudFormation / Terraform Example

# VPC and Networking
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true
  
  tags = {
    Name = "scaleplus-vpc"
  }
}

# Public Subnets
resource "aws_subnet" "public" {
  count             = 2
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.${count.index + 1}.0/24"
  availability_zone = data.aws_availability_zones.available.names[count.index]
  
  map_public_ip_on_launch = true
  
  tags = {
    Name = "scaleplus-public-${count.index + 1}"
    Type = "Public"
  }
}

# Application Load Balancer
resource "aws_lb" "main" {
  name               = "scaleplus-alb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.alb.id]
  subnets            = aws_subnet.public[*].id
  
  enable_deletion_protection = true
  
  access_logs {
    bucket  = aws_s3_bucket.logs.bucket
    prefix  = "alb-logs"
    enabled = true
  }
}

# ECS Cluster (Container Orchestration)
resource "aws_ecs_cluster" "main" {
  name = "scaleplus-cluster"
  
  setting {
    name  = "containerInsights"
    value = "enabled"
  }
}

# ECS Service
resource "aws_ecs_service" "app" {
  name            = "scaleplus-app"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.app.arn
  desired_count   = 3
  launch_type     = "FARGATE"
  
  network_configuration {
    subnets          = aws_subnet.private[*].id
    security_groups  = [aws_security_group.app.id]
    assign_public_ip = false
  }
  
  load_balancer {
    target_group_arn = aws_lb_target_group.app.arn
    container_name   = "app"
    container_port   = 3000
  }
  
  deployment_controller {
    type = "ECS"
  }
}

# Auto Scaling
resource "aws_appautoscaling_target" "app" {
  max_capacity       = 10
  min_capacity       = 3
  resource_id        = "service/${aws_ecs_cluster.main.name}/${aws_ecs_service.app.name}"
  scalable_dimension = "ecs:service:DesiredCount"
  service_namespace  = "ecs"
}

resource "aws_appautoscaling_policy" "cpu" {
  name               = "scaleplus-cpu-autoscaling"
  policy_type        = "TargetTrackingScaling"
  resource_id        = aws_appautoscaling_target.app.resource_id
  scalable_dimension = aws_appautoscaling_target.app.scalable_dimension
  service_namespace  = aws_appautoscaling_target.app.service_namespace
  
  target_tracking_scaling_policy_configuration {
    predefined_metric_specification {
      predefined_metric_type = "ECSServiceAverageCPUUtilization"
    }
    target_value = 70.0
  }
}

# RDS Database
resource "aws_db_instance" "main" {
  identifier           = "scaleplus-db"
  engine              = "postgres"
  engine_version      = "15.0"
  instance_class      = "db.t3.medium"
  allocated_storage   = 100
  storage_type        = "gp3"
  
  db_name  = "scaleplus"
  username = "dbadmin"
  password = random_password.db_password.result
  
  multi_az               = true
  publicly_accessible    = false
  vpc_security_group_ids = [aws_security_group.db.id]
  db_subnet_group_name   = aws_db_subnet_group.main.name
  
  backup_retention_period = 7
  backup_window          = "03:00-04:00"
  maintenance_window     = "Mon:04:00-Mon:05:00"
  
  encrypted = true
  
  deletion_protection = true
  skip_final_snapshot = false
}

# ElastiCache (Redis)
resource "aws_elasticache_cluster" "redis" {
  cluster_id           = "scaleplus-redis"
  engine              = "redis"
  node_type           = "cache.t3.micro"
  num_cache_nodes     = 2
  parameter_group_name = "default.redis7"
  port                = 6379
  
  security_group_ids = [aws_security_group.redis.id]
  subnet_group_name  = aws_elasticache_subnet_group.main.name
}

# S3 Bucket for Assets
resource "aws_s3_bucket" "assets" {
  bucket = "scaleplus-assets-prod"
}

resource "aws_s3_bucket_versioning" "assets" {
  bucket = aws_s3_bucket.assets.id
  versioning_configuration {
    status = "Enabled"
  }
}

# CloudFront CDN
resource "aws_cloudfront_distribution" "cdn" {
  origin {
    domain_name = aws_s3_bucket.assets.bucket_regional_domain_name
    origin_id   = "S3-assets"
    
    s3_origin_config {
      origin_access_identity = aws_cloudfront_origin_access_identity.main.cloudfront_access_identity_path
    }
  }
  
  enabled             = true
  is_ipv6_enabled     = true
  default_root_object = "index.html"
  
  default_cache_behavior {
    allowed_methods  = ["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "S3-assets"
    
    forwarded_values {
      query_string = false
      cookies {
        forward = "none"
      }
    }
    
    viewer_protocol_policy = "redirect-to-https"
    min_ttl                = 0
    default_ttl            = 3600
    max_ttl                = 86400
  }
  
  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }
  
  viewer_certificate {
    cloudfront_default_certificate = false
    acm_certificate_arn           = aws_acm_certificate.main.arn
    ssl_support_method            = "sni-only"
    minimum_protocol_version      = "TLSv1.2_2021"
  }
}
"""


# ============== System Design Patterns ==============

class SystemDesignPatterns:
    """Common system design patterns."""
    
    # 1. Load Balancing Algorithms
    LOAD_BALANCING = {
        "round_robin": "Distribute requests sequentially across servers",
        "least_connections": "Send to server with fewest active connections",
        "ip_hash": "Route based on client IP (session persistence)",
        "weighted": "Distribute based on server capacity weights"
    }
    
    # 2. Caching Strategies
    CACHING = {
        "cache_aside": "Application manages cache, loads on miss",
        "write_through": "Write to cache and DB simultaneously",
        "write_behind": "Write to cache, async write to DB",
        "read_through": "Cache loads from DB on miss automatically"
    }
    
    # 3. Database Scaling
    DB_SCALING = {
        "read_replicas": "Primary for writes, replicas for reads",
        "sharding": "Split data across multiple databases by key",
        "partitioning": "Split tables by row ranges or lists",
        "federation": "Different databases for different domains"
    }
    
    # 4. Microservices Patterns
    MICROSERVICES = {
        "api_gateway": "Single entry point, routes to services",
        "service_discovery": "Dynamic service location lookup",
        "circuit_breaker": "Fail fast when service is down",
        "bulkhead": "Isolate failures to prevent cascade",
        "retry": "Automatic retry with exponential backoff",
        "timeout": "Fail if response takes too long"
    }


# ============== Monitoring & Logging ==============

MONITORING_SETUP = """
# Prometheus + Grafana Monitoring
# prometheus.yml configuration
# global:
#   scrape_interval: 15s
#   evaluation_interval: 15s
# 
# scrape_configs:
#   - job_name: 'prometheus'
#     static_configs:
#       - targets: ['localhost:9090']
#   - job_name: 'node-exporter'
#     static_configs:
#       - targets: ['node-exporter:9100']
#   - job_name: 'app'
#     static_configs:
#       - targets: ['app:3000']
#     metrics_path: '/metrics'
"""

# Key Metrics to Track:
METRICS = {
    "infrastructure": [
        "CPU utilization",
        "Memory usage",
        "Disk I/O",
        "Network throughput"
    ],
    "application": [
        "Request rate (RPS)",
        "Response time (p50, p95, p99)",
        "Error rate",
        "Active connections"
    ],
    "business": [
        "User signups",
        "Task completions",
        "Revenue per hour"
    ]
}

# Alerting Rules:
ALERTING = """
groups:
  - name: scaleplus-alerts
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate detected"
          
      - alert: HighResponseTime
        expr: histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m])) > 0.5
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "95th percentile latency > 500ms"
          
      - alert: DatabaseConnectionsHigh
        expr: pg_stat_activity_count > 80
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Database connection pool near limit"
"""


# ============== Security Best Practices ==============

SECURITY_CHECKLIST = """
# Security Best Practices

## Application Security
- [ ] Input validation on all endpoints
- [ ] Parameterized queries (prevent SQL injection)
- [ ] XSS protection (sanitize output)
- [ ] CSRF tokens for state-changing operations
- [ ] Content Security Policy headers
- [ ] Rate limiting on all endpoints
- [ ] Strong password policies
- [ ] Multi-factor authentication (MFA)

## Infrastructure Security
- [ ] HTTPS everywhere (TLS 1.2+)
- [ ] Secrets management (AWS Secrets Manager, Vault)
- [ ] Network segmentation (VPC, security groups)
- [ ] WAF (Web Application Firewall)
- [ ] DDoS protection (AWS Shield, CloudFlare)
- [ ] Regular security scans (Snyk, Trivy)
- [ ] Container image scanning

## Data Security
- [ ] Encryption at rest (AES-256)
- [ ] Encryption in transit (TLS)
- [ ] Database encryption
- [ ] Backup encryption
- [ ] PII data handling compliance (GDPR)
- [ ] Data retention policies

## Operational Security
- [ ] Principle of least privilege
- [ ] Regular access reviews
- [ ] Audit logging
- [ ] Incident response plan
- [ ] Security training for team
"""


# ============== Main ==============

async def main():
    """Demonstrate Phase 3 DevOps concepts."""
    print("=" * 70)
    print("FULLSTACK MASTERY - PHASE 3: DEVOPS & SYSTEM DESIGN")
    print("=" * 70)
    
    # 1. CI/CD
    print("\n1. CI/CD PIPELINE")
    print("-" * 40)
    print("   GitHub Actions workflow includes:")
    print("     • Build stage (lint, compile)")
    print("     • Test stage (unit, integration)")
    print("     • Security stage (audit, Snyk scan)")
    print("     • Deploy stage (staging, production)")
    print("   Features:")
    print("     • Caching for faster builds")
    print("     • Artifact uploads")
    print("     • Code coverage reporting")
    print("     • Environment protection rules")
    
    # 2. Docker
    print("\n2. DOCKER CONTAINERIZATION")
    print("-" * 40)
    print("   Multi-stage Dockerfile:")
    print("     • Builder stage: Compile application")
    print("     • Production stage: Minimal runtime image")
    print("   Security features:")
    print("     • Non-root user (nodejs)")
    print("     • Read-only root filesystem")
    print("     • Health checks")
    print("   Docker Compose:")
    print("     • App, Database, Redis, Nginx services")
    print("     • Resource limits and reservations")
    print("     • Persistent volumes")
    
    # 3. Kubernetes
    print("\n3. KUBERNETES ORCHESTRATION")
    print("-" * 40)
    print("   Deployment features:")
    print("     • 3 replicas for high availability")
    print("     • Rolling update strategy")
    print("     • Liveness and readiness probes")
    print("     • Resource limits and requests")
    print("     • Security contexts (non-root)")
    print("   Service & Ingress:")
    print("     • ClusterIP for internal communication")
    print("     • Ingress with SSL termination")
    print("     • Rate limiting annotations")
    
    # 4. Cloud Architecture
    print("\n4. AWS CLOUD ARCHITECTURE")
    print("-" * 40)
    print("   Components:")
    print("     • VPC with public/private subnets")
    print("     • Application Load Balancer")
    print("     • ECS Fargate (serverless containers)")
    print("     • RDS PostgreSQL (Multi-AZ)")
    print("     • ElastiCache Redis")
    print("     • S3 for asset storage")
    print("     • CloudFront CDN")
    print("   Features:")
    print("     • Auto-scaling based on CPU")
    print("     • Encrypted storage")
    print("     • Backup and recovery")
    print("     • DDoS protection")
    
    # 5. System Design Patterns
    print("\n5. SYSTEM DESIGN PATTERNS")
    print("-" * 40)
    print("   Load Balancing:")
    for name, desc in SystemDesignPatterns.LOAD_BALANCING.items():
        print(f"     • {name}: {desc}")
    print("\n   Caching Strategies:")
    for name, desc in SystemDesignPatterns.CACHING.items():
        print(f"     • {name}: {desc}")
    print("\n   Microservices Patterns:")
    for name, desc in SystemDesignPatterns.MICROSERVICES.items():
        print(f"     • {name}: {desc}")
    
    # 6. Monitoring
    print("\n6. MONITORING & OBSERVABILITY")
    print("-" * 40)
    print("   Prometheus metrics collection:")
    for category, metrics in METRICS.items():
        print(f"     {category}:")
        for metric in metrics:
            print(f"       - {metric}")
    print("\n   Alerting rules:")
    print("     • High error rate (> 5%)")
    print("     • High response time (> 500ms p95)")
    print("     • Database connection pool near limit")
    
    # 7. Security
    print("\n7. SECURITY BEST PRACTICES")
    print("-" * 40)
    print("   Application Security:")
    print("     • Input validation")
    print("     • SQL injection prevention")
    print("     • XSS protection")
    print("     • CSRF tokens")
    print("   Infrastructure Security:")
    print("     • HTTPS everywhere")
    print("     • Secrets management")
    print("     • Network segmentation")
    print("     • WAF and DDoS protection")
    
    print("\n" + "=" * 70)
    print("PHASE 3 CONCEPTS DEMONSTRATED:")
    print("=" * 70)
    concepts = [
        "CI/CD Pipeline Design (GitHub Actions)",
        "Build, Test, Security, Deploy stages",
        "Docker Multi-stage Builds",
        "Docker Compose Orchestration",
        "Kubernetes Deployments",
        "Service Discovery & Ingress",
        "Auto-scaling Configuration",
        "AWS Cloud Architecture",
        "VPC, ALB, ECS, RDS Design",
        "CDN with CloudFront",
        "Load Balancing Algorithms",
        "Caching Strategies",
        "Database Scaling Patterns",
        "Microservices Architecture",
        "Circuit Breaker Pattern",
        "Prometheus Monitoring",
        "Grafana Dashboards",
        "Alerting Rules",
        "Security Best Practices",
        "Infrastructure as Code"
    ]
    for i, concept in enumerate(concepts, 1):
        print(f"  {i:2}. {concept}")
    
    print("\n" + "=" * 70)
    print("FULLSTACK MASTERY COMPLETE!")
    print("=" * 70)
    print("\n3 Phases, Full-Stack Development Mastery:")
    print("  Phase 1: Frontend (HTML, CSS, JS, TypeScript, React)")
    print("  Phase 2: Backend (FastAPI, DB, Auth, GraphQL, WebSockets)")
    print("  Phase 3: DevOps (CI/CD, Docker, K8s, Cloud, Monitoring)")
    print("\nReady to build production-grade applications!")


if __name__ == "__main__":
    asyncio.run(main())
