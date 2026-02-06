#!/usr/bin/env python3
"""
Security Mastery - Application & Infrastructure Security
Best practices for secure development
"""

import asyncio
import hashlib
import hmac
import secrets
from typing import Dict, List, Any
from dataclasses import dataclass
from enum import Enum


# ============== OWASP Top 10 ==============

class OWASPTopTen:
    """OWASP Top 10 2021 vulnerabilities and mitigations."""
    
    VULNERABILITIES = {
        "A01:2021-Broken Access Control": {
            "description": "Restrictions on authenticated users are not properly enforced",
            "examples": [
                "IDOR: User can access /api/users/123/data when they should only access /api/users/456/data",
                "Elevation of privilege: Regular user can access admin endpoints",
                "JWT manipulation: Modify token claims to change user role"
            ],
            "mitigations": [
                "Deny by default - whitelist allowed actions",
                "Implement proper authorization checks on every endpoint",
                "Use framework's built-in authorization",
                "Implement rate limiting",
                "Invalidate sessions server-side on logout"
            ]
        },
        "A02:2021-Cryptographic Failures": {
            "description": "Sensitive data exposed or improperly protected",
            "examples": [
                "Storing passwords in plain text",
                "Using weak hashing (MD5, SHA1) for passwords",
                "Unencrypted database connections",
                "Missing TLS/SSL"
            ],
            "mitigations": [
                "Use strong hashing (Argon2, bcrypt, scrypt, PBKDF2)",
                "Encrypt data at rest (AES-256)",
                "Enforce HTTPS/TLS 1.2+",
                "Use secure key management (KMS, Vault)",
                "Don't store sensitive data unnecessarily"
            ]
        },
        "A03:2021-Injection": {
            "description": "Untrusted data sent to interpreter as command",
            "examples": [
                "SQL Injection: ' OR '1'='1",
                "NoSQL Injection: {\"$ne\": null}",
                "Command Injection: ; rm -rf /",
                "LDAP Injection"
            ],
            "mitigations": [
                "Use parameterized queries (prepared statements)",
                "Use ORM with query builders",
                "Input validation and sanitization",
                "Least privilege database accounts",
                "WAF (Web Application Firewall)"
            ]
        },
        "A04:2021-Insecure Design": {
            "description": "Missing or ineffective security controls in design",
            "examples": [
                "No business logic validation",
                "Missing anti-automation controls",
                "Race conditions in financial transactions"
            ],
            "mitigations": [
                "Threat modeling in design phase",
                "Secure design patterns",
                "Principle of least privilege",
                "Defense in depth",
                "Unit/integration security tests"
            ]
        },
        "A05:2021-Security Misconfiguration": {
            "description": "Improper security configurations",
            "examples": [
                "Default credentials",
                "Unnecessary features enabled",
                "Verbose error messages",
                "Cloud storage publicly accessible"
            ],
            "mitigations": [
                "Hardened base images",
                "Automated security scanning",
                "Remove unused dependencies",
                "Environment-specific configs",
                "Regular security audits"
            ]
        },
        "A06:2021-Vulnerable Components": {
            "description": "Using components with known vulnerabilities",
            "examples": [
                "Outdated libraries with CVEs",
                "Abandoned dependencies",
                "Vulnerable Docker base images"
            ],
            "mitigations": [
                "Dependency scanning (Snyk, Dependabot)",
                "Software Bill of Materials (SBOM)",
                "Automated updates for security patches",
                "Container image scanning",
                "Minimal base images"
            ]
        },
        "A07:2021-Authentication Failures": {
            "description": "Authentication weaknesses allowing compromise",
            "examples": [
                "Brute force attacks on login",
                "Weak password policies",
                "Session fixation",
                "Credential stuffing"
            ],
            "mitigations": [
                "Multi-factor authentication (MFA)",
                "Strong password policies",
                "Rate limiting on auth endpoints",
                "Secure session management",
                "Account lockout policies"
            ]
        },
        "A08:2021-Integrity Failures": {
            "description": "Software and data integrity failures",
            "examples": [
                "Insecure deserialization",
                "Unsigned updates",
                "Dependency confusion attacks"
            ],
            "mitigations": [
                "Digitally sign updates",
                "Verify dependencies integrity",
                "Use integrity hashes for CDNs",
                "Secure CI/CD pipelines",
                "Code signing"
            ]
        },
        "A09:2021-Logging Failures": {
            "description": "Insufficient logging and monitoring",
            "examples": [
                "No audit logs for sensitive actions",
                "Logs not monitored",
                "Insufficient forensic data"
            ],
            "mitigations": [
                "Comprehensive audit logging",
                "Centralized log aggregation",
                "Real-time alerting",
                "Tamper-proof logs",
                "SIEM integration"
            ]
        },
        "A10:2021-SSRF": {
            "description": "Server-Side Request Forgery",
            "examples": [
                "Fetching internal services via URL parameter",
                "Accessing cloud metadata endpoints",
                "Port scanning via URL"
            ],
            "mitigations": [
                "URL validation and sanitization",
                "Deny by default - whitelist allowed URLs",
                "Network segmentation",
                "Disable unnecessary URL schemes",
                "Use internal DNS resolution"
            ]
        }
    }


# ============== Secure Coding Practices ==============

class SecureCoding:
    """Secure coding guidelines by language."""
    
    PYTHON_SECURE = """
    # Python Secure Coding
    
    # 1. Input Validation
    import re
    from pydantic import BaseModel, validator
    
    class UserInput(BaseModel):
        username: str
        email: str
        age: int
        
        @validator('username')
        def validate_username(cls, v):
            if not re.match(r'^[a-zA-Z0-9_]{3,20}$', v):
                raise ValueError('Invalid username')
            return v
        
        @validator('email')
        def validate_email(cls, v):
            if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$', v):
                raise ValueError('Invalid email')
            return v
    
    # 2. SQL Injection Prevention
    # BAD:
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    
    # GOOD:
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    
    # 3. Password Hashing
    import bcrypt
    
    def hash_password(password: str) -> str:
        salt = bcrypt.gensalt(rounds=12)
        return bcrypt.hashpw(password.encode(), salt).decode()
    
    def verify_password(password: str, hashed: str) -> bool:
        return bcrypt.checkpw(password.encode(), hashed.encode())
    
    # 4. Secure Random Generation
    import secrets
    
    token = secrets.token_urlsafe(32)  # For URLs
    otp = secrets.randbelow(1000000)   # For OTPs
    
    # 5. Safe File Operations
    import os
    from pathlib import Path
    
    def safe_file_access(filename: str, base_dir: str) -> bool:
        # Prevent directory traversal
        full_path = Path(base_dir) / filename
        try:
            full_path.resolve().relative_to(Path(base_dir).resolve())
            return True
        except ValueError:
            return False  # Path traversal attempt
    
    # 6. Deserialization Safety
    import json
    
    # BAD (Python-specific vulnerability):
    # data = pickle.loads(untrusted_data)
    
    # GOOD:
    data = json.loads(untrusted_data)
    
    # 7. Secrets Management
    from cryptography.fernet import Fernet
    
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted = cipher.encrypt(b"Sensitive data")
    decrypted = cipher.decrypt(encrypted)
    """
    
    JAVASCRIPT_SECURE = """
    // JavaScript/Node.js Secure Coding
    
    // 1. Input Validation
    const Joi = require('joi');
    
    const schema = Joi.object({
        username: Joi.string().alphanum().min(3).max(30).required(),
        email: Joi.string().email().required(),
        password: Joi.string().pattern(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{8,}$/),
        role: Joi.string().valid('user', 'admin').default('user')
    });
    
    const { error, value } = schema.validate(req.body);
    if (error) {
        return res.status(400).json({ error: error.details[0].message });
    }
    
    // 2. SQL Injection Prevention (using parameterized queries)
    // BAD:
    db.query(`SELECT * FROM users WHERE id = ${userId}`);
    
    // GOOD:
    db.query('SELECT * FROM users WHERE id = ?', [userId]);
    
    // 3. Password Hashing
    const bcrypt = require('bcrypt');
    const saltRounds = 12;
    
    async function hashPassword(password) {
        return await bcrypt.hash(password, saltRounds);
    }
    
    async function verifyPassword(password, hash) {
        return await bcrypt.compare(password, hash);
    }
    
    // 4. XSS Prevention
    const escapeHtml = (unsafe) => {
        return unsafe
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    };
    
    // Or use template engines that auto-escape
    // EJS, Handlebars, React (JSX escapes by default)
    
    // 5. Secure Headers
    const helmet = require('helmet');
    app.use(helmet({
        contentSecurityPolicy: {
            directives: {
                defaultSrc: ["'self'"],
                scriptSrc: ["'self'", "'unsafe-inline'"],
                styleSrc: ["'self'", "'unsafe-inline'"],
                imgSrc: ["'self'", "data:", "https:"],
            },
        },
        hsts: {
            maxAge: 31536000,
            includeSubDomains: true,
            preload: true
        }
    }));
    
    // 6. JWT Security
    const jwt = require('jsonwebtoken');
    
    // Sign with strong secret, short expiry
    const token = jwt.sign(
        { userId: user.id, role: user.role },
        process.env.JWT_SECRET,
        { expiresIn: '15m', algorithm: 'HS256' }
    );
    
    // Verify and handle errors
    try {
        const decoded = jwt.verify(token, process.env.JWT_SECRET);
    } catch (err) {
        if (err.name === 'TokenExpiredError') {
            return res.status(401).json({ error: 'Token expired' });
        }
        return res.status(401).json({ error: 'Invalid token' });
    }
    """


# ============== Authentication & Authorization ==============

class AuthSecurity:
    """Authentication and authorization best practices."""
    
    JWT_BEST_PRACTICES = """
    # JWT Security Best Practices
    
    1. Algorithm
       - Use HS256 or RS256
       - NEVER use 'none' algorithm
       - Validate algorithm in header
    
    2. Secrets
       - Use strong, random secrets (256+ bits)
       - Store in environment variables / secrets manager
       - Rotate periodically
       - Different secrets per environment
    
    3. Claims
       - Use short expiration (15-30 minutes)
       - Include 'iat' (issued at), 'exp' (expiration), 'sub' (subject)
       - Don't include sensitive data in payload (it's just base64)
       - Use 'jti' (JWT ID) for token revocation
    
    4. Refresh Tokens
       - Store securely (httpOnly cookies)
       - One-time use
       - Short expiration (7 days)
       - Rotate on use
       - Bind to device/session
    
    5. Validation
       - Verify signature
       - Check expiration
       - Validate issuer (iss)
       - Validate audience (aud)
       - Check if token is revoked
    """
    
    OAUTH2_FLOW = """
    # OAuth 2.0 / OpenID Connect
    
    ## Authorization Code Flow (Recommended for SPAs)
    
    1. User clicks "Login with Provider"
    2. Redirect to Authorization Server:
       GET https://auth.provider.com/authorize?
         response_type=code&
         client_id=CLIENT_ID&
         redirect_uri=https://app.com/callback&
         scope=openid profile email&
         state=RANDOM_STATE&
         code_challenge=PKCE_CHALLENGE
    
    3. User authenticates and consents
    4. Authorization Server redirects with code:
       GET https://app.com/callback?
         code=AUTH_CODE&
         state=RANDOM_STATE
    
    5. Backend exchanges code for tokens:
       POST https://auth.provider.com/token
       {
         "grant_type": "authorization_code",
         "code": AUTH_CODE,
         "redirect_uri": "https://app.com/callback",
         "client_id": CLIENT_ID,
         "client_secret": CLIENT_SECRET,
         "code_verifier": PKCE_VERIFIER
       }
    
    6. Response:
       {
         "access_token": "...",
         "refresh_token": "...",
         "id_token": "JWT with user info",
         "expires_in": 3600
       }
    
    ## Security Considerations
    - Always use PKCE for public clients
    - Validate state parameter (CSRF protection)
    - Use exact redirect_uri match
    - Store tokens securely
    - Short-lived access tokens
    """
    
    RBAC_ABAC = """
    # Authorization Models
    
    ## RBAC (Role-Based Access Control)
    
    Roles:
      - admin: Can do everything
      - manager: Can manage users, view reports
      - user: Can manage own tasks
      - guest: Read-only
    
    Permissions:
      - task:create
      - task:read
      - task:update
      - task:delete
      - user:create
      - user:delete
    
    Role-Permission Mapping:
      admin: [all permissions]
      manager: [task:*, user:create, user:read]
      user: [task:create, task:read, task:update:own]
    
    ## ABAC (Attribute-Based Access Control)
    
    More flexible, considers:
      - Subject attributes: role, department, clearance
      - Resource attributes: owner, classification, status
      - Action: read, write, delete
      - Environment: time, location, device
    
    Example Policy:
      "Allow IF:
        user.role == 'manager' AND
        user.department == resource.department AND
        time.hour >= 9 AND time.hour <= 17"
    
    ## Implementation
    
    # Middleware approach
    @require_role('admin')
    def delete_user(user_id):
        pass
    
    @require_permission('task:update')
    def update_task(task_id):
        pass
    
    # Decorator with ownership check
    @require_owner_or_role(Task, 'admin')
    def update_task(task_id):
        pass
    """


# ============== Infrastructure Security ==============

class InfrastructureSecurity:
    """Cloud and infrastructure security."""
    
    CLOUD_SECURITY = """
    # AWS Security Best Practices
    
    ## IAM (Identity and Access Management)
    - Use IAM roles for EC2/ECS/Lambda (not access keys)
    - Principle of least privilege
    - Enable MFA for root and admin users
    - Regular access key rotation
    - Use IAM Policy Conditions
    
    Example Policy:
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:GetObject",
                    "s3:PutObject"
                ],
                "Resource": "arn:aws:s3:::mybucket/*",
                "Condition": {
                    "StringEquals": {
                        "s3:x-amz-acl": "private"
                    },
                    "Bool": {
                        "aws:SecureTransport": "true"
                    }
                }
            }
        ]
    }
    
    ## Network Security
    - VPC with private subnets for databases
    - Security groups (stateful firewall)
    - Network ACLs (stateless, subnet-level)
    - AWS WAF for web applications
    - Shield for DDoS protection
    
    ## Data Protection
    - Encrypt data at rest (KMS)
    - Encrypt data in transit (TLS)
    - Secrets Manager for credentials
    - S3 bucket policies (block public access)
    
    ## Monitoring
    - CloudTrail for API auditing
    - GuardDuty for threat detection
    - Config for compliance
    - Security Hub for centralized view
    """
    
    CONTAINER_SECURITY = """
    # Docker & Kubernetes Security
    
    ## Dockerfile Security
    - Use minimal base images (alpine, distroless)
    - Pin image versions (don't use 'latest')
    - Run as non-root user
    - Multi-stage builds (don't ship build tools)
    - Scan images for vulnerabilities
    
    Example:
    FROM node:18-alpine AS builder
    WORKDIR /app
    COPY package*.json ./
    RUN npm ci --only=production
    
    FROM node:18-alpine
    RUN addgroup -g 1001 -S nodejs
    RUN adduser -S nodejs -u 1001
    WORKDIR /app
    COPY --from=builder --chown=nodejs:nodejs /app .
    USER nodejs
    EXPOSE 3000
    CMD ["node", "server.js"]
    
    ## Kubernetes Security
    - Pod Security Standards (restricted)
    - Network policies
    - RBAC for cluster access
    - Secrets encryption at rest
    - Container runtime security (Falco)
    - Image pull policies
    
    Security Context:
    apiVersion: v1
    kind: Pod
    spec:
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
        fsGroup: 2000
      containers:
      - name: app
        image: myapp:latest
        securityContext:
          allowPrivilegeEscalation: false
          readOnlyRootFilesystem: true
          capabilities:
            drop:
            - ALL
    """


# ============== Security Testing ==============

class SecurityTesting:
    """Security testing methodologies."""
    
    TESTING_METHODS = {
        "SAST": {
            "name": "Static Application Security Testing",
            "description": "Analyze source code for vulnerabilities",
            "tools": ["SonarQube", "Checkmarx", "Semgrep", "Bandit (Python)"],
            "when": "During development / CI"
        },
        "DAST": {
            "name": "Dynamic Application Security Testing",
            "description": "Test running application for vulnerabilities",
            "tools": ["OWASP ZAP", "Burp Suite", "Nikto"],
            "when": "Staging / Pre-production"
        },
        "SCA": {
            "name": "Software Composition Analysis",
            "description": "Identify vulnerable dependencies",
            "tools": ["Snyk", "OWASP Dependency-Check", "npm audit"],
            "when": "Continuous"
        },
        "Container_Scanning": {
            "name": "Container Image Scanning",
            "description": "Find vulnerabilities in Docker images",
            "tools": ["Trivy", "Clair", "Aqua Security"],
            "when": "CI / Before deployment"
        },
        "Penetration_Testing": {
            "name": "Penetration Testing",
            "description": "Manual security assessment",
            "tools": ["Burp Suite Pro", "Metasploit", "Custom scripts"],
            "when": "Periodic (quarterly)"
        },
        "Fuzzing": {
            "name": "Fuzz Testing",
            "description": "Input random data to find crashes",
            "tools": ["AFL", "libFuzzer", "Boofuzz"],
            "when": "Testing phase"
        }
    }


# ============== Main ==============

async def main():
    """Demonstrate security mastery."""
    print("=" * 70)
    print("SECURITY MASTERY - APPLICATION & INFRASTRUCTURE")
    print("=" * 70)
    
    # 1. OWASP Top 10
    print("\n1. OWASP TOP 10 (2021)")
    print("-" * 40)
    for vuln, info in list(OWASPTopTen.VULNERABILITIES.items())[:3]:
        print(f"\n   {vuln}:")
        print(f"     {info['description'][:60]}...")
        print(f"     Mitigation: {info['mitigations'][0]}")
    
    # 2. Secure Coding
    print("\n2. SECURE CODING PRACTICES")
    print("-" * 40)
    practices = [
        "Input validation (whitelist approach)",
        "Parameterized queries (prevent SQLi)",
        "Strong password hashing (Argon2/bcrypt)",
        "Secure random generation",
        "XSS prevention (output encoding)",
        "Secure HTTP headers (CSP, HSTS)",
        "Safe deserialization"
    ]
    for practice in practices:
        print(f"     • {practice}")
    
    # 3. Auth Security
    print("\n3. AUTHENTICATION & AUTHORIZATION")
    print("-" * 40)
    print("   JWT Best Practices:")
    jwt_practices = [
        "Use HS256 or RS256 (never 'none')",
        "Short expiration (15-30 min)",
        "Secure secrets (256+ bits)",
        "Validate all claims",
        "Implement token revocation"
    ]
    for practice in jwt_practices:
        print(f"     • {practice}")
    
    print("\n   Authorization Models:")
    print(f"     • RBAC: Role-Based Access Control")
    print(f"     • ABAC: Attribute-Based Access Control")
    
    # 4. Infrastructure Security
    print("\n4. INFRASTRUCTURE SECURITY")
    print("-" * 40)
    print("   Container Security:")
    container_security = [
        "Minimal base images (alpine/distroless)",
        "Run as non-root user",
        "Read-only root filesystem",
        "Drop all capabilities",
        "No privilege escalation"
    ]
    for item in container_security:
        print(f"     • {item}")
    
    # 5. Security Testing
    print("\n5. SECURITY TESTING")
    print("-" * 40)
    for method, info in SecurityTesting.TESTING_METHODS.items():
        print(f"   {method}: {info['name']}")
        print(f"     Tools: {', '.join(info['tools'][:2])}")
    
    print("\n" + "=" * 70)
    print("SECURITY CONCEPTS DEMONSTRATED:")
    print("=" * 70)
    concepts = [
        "OWASP Top 10 vulnerabilities",
        "Injection attack prevention",
        "Authentication bypass protection",
        "Cryptographic failures mitigation",
        "Secure session management",
        "Input validation patterns",
        "Password hashing (bcrypt, Argon2)",
        "JWT security best practices",
        "OAuth 2.0 / OIDC flow",
        "RBAC and ABAC authorization",
        "Cloud security (AWS)",
        "Container security",
        "Kubernetes security contexts",
        "SAST, DAST, SCA testing",
        "Penetration testing",
        "Security scanning automation"
    ]
    for i, concept in enumerate(concepts, 1):
        print(f"  {i:2}. {concept}")
    
    print("\n" + "=" * 70)
    print("SECURITY MASTERY COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    asyncio.run(main())
