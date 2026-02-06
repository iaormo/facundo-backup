#!/usr/bin/env python3
"""
Database Mastery - Phase 2: Performance & High Availability
Replication, Sharding, Performance Tuning
"""

import asyncio
from dataclasses import dataclass
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime
from enum import Enum


# ============== Database Replication ==============

class ReplicationTopologies:
    """Database replication patterns."""
    
    TOPOLOGIES = {
        "master_slave": {
            "description": "One master for writes, multiple slaves for reads",
            "pros": ["Simple setup", "Read scaling", "Backup from slave"],
            "cons": ["Manual failover", "Replication lag", "Single write point"],
            "use_case": "Read-heavy applications, reporting"
        },
        "master_master": {
            "description": "Multiple masters accepting writes",
            "pros": ["High availability", "Write scaling", "Automatic failover"],
            "cons": ["Conflict resolution needed", "Complex setup", "Split-brain risk"],
            "use_case": "Global applications, high availability requirements"
        },
        "circular": {
            "description": "Each node replicates to the next in a circle",
            "pros": ["No single point of failure", "Good for multi-region"],
            "cons": ["Complex conflict resolution", "Difficult to troubleshoot"],
            "use_case": "Multi-region deployments"
        },
        "tree": {
            "description": "Hierarchical replication",
            "pros": ["Scales to many slaves", "Reduces master load"],
            "cons": ["Increased replication lag", "Complex topology"],
            "use_case": "Very large deployments"
        }
    }
    
    POSTGRESQL_REPLICATION = """
    -- Streaming Replication Setup (PostgreSQL)
    
    -- On Master (postgresql.conf):
    wal_level = replica
    max_wal_senders = 10
    max_replication_slots = 10
    wal_keep_size = 1GB
    hot_standby = on
    
    -- Create replication user
    CREATE USER replicator WITH REPLICATION ENCRYPTED PASSWORD 'secret';
    
    -- pg_hba.conf:
    host replication replicator 10.0.0.0/24 scram-sha-256
    
    -- On Replica:
    -- 1. Stop PostgreSQL
    -- 2. Clear data directory
    -- 3. pg_basebackup from master
    pg_basebackup -h master-host -D /var/lib/postgresql/data -U replicator -P -v -R
    
    -- 4. Start PostgreSQL
    -- Replica now streams from master
    
    -- Check replication status on master:
    SELECT * FROM pg_stat_replication;
    
    -- Check replication lag:
    SELECT 
        client_addr,
        state,
        sent_lsn, 
        write_lsn,
        flush_lsn,
        replay_lsn,
        pg_size_pretty(pg_wal_lsn_diff(sent_lsn, replay_lsn)) as lag
    FROM pg_stat_replication;
    
    -- Logical Replication (table-level)
    -- On Publisher:
    CREATE PUBLICATION mypub FOR TABLE tasks, users;
    
    -- On Subscriber:
    CREATE SUBSCRIPTION mysub 
    CONNECTION 'host=publisher-host dbname=mydb user=replicator'
    PUBLICATION mypub;
    """
    
    MYSQL_REPLICATION = """
    -- MySQL Master-Slave Replication
    
    -- On Master (my.cnf):
    [mysqld]
    server-id = 1
    log_bin = /var/log/mysql/mysql-bin
    binlog_do_db = myapp
    binlog_format = ROW
    
    -- Create replication user
    CREATE USER 'replicator'@'%' IDENTIFIED BY 'password';
    GRANT REPLICATION SLAVE ON *.* TO 'replicator'@'%';
    
    -- Get binlog position
    FLUSH TABLES WITH READ LOCK;
    SHOW MASTER STATUS;
    -- Record File and Position
    UNLOCK TABLES;
    
    -- On Slave (my.cnf):
    [mysqld]
    server-id = 2
    relay_log = /var/log/mysql/mysql-relay-bin
    log_bin = /var/log/mysql/mysql-bin
    read_only = 1
    
    -- Configure replication
    CHANGE MASTER TO
        MASTER_HOST='master-host',
        MASTER_USER='replicator',
        MASTER_PASSWORD='password',
        MASTER_LOG_FILE='mysql-bin.000001',
        MASTER_LOG_POS=154;
    
    START SLAVE;
    
    -- Check status
    SHOW SLAVE STATUS\G
    -- Check: Slave_IO_Running and Slave_SQL_Running should be Yes
    """


# ============== Database Sharding ==============

class ShardingStrategies:
    """Database sharding patterns."""
    
    STRATEGIES = {
        "hash": {
            "description": "Shard = hash(key) % num_shards",
            "pros": ["Even distribution", "Simple to implement"],
            "cons": ["Hard to add shards (resharding needed)", "Range queries expensive"],
            "example": "shard_id = hash(user_id) % 16"
        },
        "range": {
            "description": "Shard by key range (A-M, N-Z)",
            "pros": ["Efficient range queries", "Easy to add shards"],
            "cons": ["Hot spots possible", "Uneven distribution"],
            "example": "Users A-G: shard1, H-N: shard2, O-Z: shard3"
        },
        "list": {
            "description": "Shard by category (geography, tenant)",
            "pros": ["Data locality", "Easy to understand"],
            "cons": ["Manual assignment", "Uneven distribution"],
            "example": "US users: shard1, EU users: shard2, Asia: shard3"
        },
        "composite": {
            "description": "Combine multiple strategies",
            "pros": ["Flexibility", "Optimized for access patterns"],
            "cons": ["Complexity", "Harder to manage"],
            "example": "Tenant ID for shard, then user_id hash within shard"
        }
    }
    
    SHARDING_SQL = """
    -- Sharding Implementation Example (Application-level)
    
    -- Determine shard for user
    CREATE OR REPLACE FUNCTION get_shard_id(user_id BIGINT)
    RETURNS INTEGER AS $$
    BEGIN
        RETURN user_id % 16;  -- 16 shards
    END;
    $$ LANGUAGE plpgsql;
    
    -- Sharded table schema (same on all shards)
    CREATE TABLE users_0 (LIKE users INCLUDING ALL);
    CREATE TABLE users_1 (LIKE users INCLUDING ALL);
    -- ... up to users_15
    
    -- Application logic (pseudo-code):
    -- def get_user(user_id):
    --     shard_id = user_id % 16
    --     db = shard_connections[shard_id]
    --     return db.query("SELECT * FROM users WHERE id = ?", user_id)
    
    -- Cross-shard queries (coordinator node):
    -- UNION ALL across shards
    SELECT * FROM users_0 WHERE email = 'test@example.com'
    UNION ALL
    SELECT * FROM users_1 WHERE email = 'test@example.com'
    -- ... etc
    
    -- Rebalancing shards:
    -- 1. Create new shard
    -- 2. Copy subset of data to new shard
    -- 3. Update shard map
    -- 4. Delete moved data from old shard
    -- 5. Use consistent hashing to minimize data movement
    """


# ============== Performance Tuning ==============

class PerformanceTuning:
    """Database performance optimization."""
    
    POSTGRESQL_TUNING = """
    -- postgresql.conf optimization
    
    -- Memory Settings
    shared_buffers = 4GB                    # 25% of RAM
    effective_cache_size = 12GB             # 75% of RAM
    work_mem = 64MB                         # Per operation
    maintenance_work_mem = 512MB            # For VACUUM, CREATE INDEX
    
    -- WAL Settings
    wal_buffers = 16MB
    max_wal_size = 4GB
    min_wal_size = 1GB
    checkpoint_completion_target = 0.9
    
    -- Query Planning
    random_page_cost = 1.1                  # For SSD (4.0 for HDD)
    effective_io_concurrency = 200          # For SSD
    default_statistics_target = 100
    
    -- Parallel Query
    max_parallel_workers_per_gather = 4
    max_parallel_workers = 8
    max_parallel_maintenance_workers = 4
    
    -- Logging
    log_min_duration_statement = 1000       # Log slow queries (>1s)
    log_checkpoints = on
    log_connections = on
    log_disconnections = on
    log_lock_waits = on
    log_temp_files = 0
    
    -- Autovacuum
    autovacuum_max_workers = 3
    autovacuum_naptime = 10s
    autovacuum_vacuum_scale_factor = 0.1
    autovacuum_analyze_scale_factor = 0.05
    """
    
    QUERY_OPTIMIZATION = """
    -- Analyze table statistics
    ANALYZE users;
    ANALYZE tasks;
    
    -- Vacuum (remove dead tuples)
    VACUUM ANALYZE users;
    VACUUM FULL users;  -- Reclaim space (locks table)
    
    -- Reindex
    REINDEX INDEX CONCURRENTLY idx_users_email;
    
    -- Partition pruning
    -- Query planner skips irrelevant partitions
    EXPLAIN SELECT * FROM events WHERE created_at >= '2024-01-01';
    -- Should show: "Partition Ref: events_2024_01"
    
    -- Parallel query
    EXPLAIN (ANALYZE, VERBOSE)
    SELECT COUNT(*) FROM large_table;
    -- Should show: "Workers Planned: 4"
    
    -- Connection pooling (PgBouncer)
    -- pgbouncer.ini:
    [databases]
    mydb = host=localhost port=5432 dbname=mydb
    
    [pgbouncer]
    listen_port = 6432
    listen_addr = 127.0.0.1
    auth_type = md5
    auth_file = /etc/pgbouncer/userlist.txt
    
    pool_mode = transaction  # session, transaction, or statement
    max_client_conn = 10000
    default_pool_size = 25
    max_db_connections = 100
    max_user_connections = 100
    
    -- Connection pool sizing formula:
    -- connections = ((core_count * 2) + effective_spindle_count)
    -- For 8 cores, SSD: (8 * 2) + 1 = 17 connections per pool
    """


# ============== High Availability ==============

class HighAvailability:
    """HA patterns and failover strategies."""
    
    PATTERNS = {
        "active_passive": {
            "description": "One active, one standby (cold spare)",
            "rto": "Minutes to hours",
            "rpo": "Possible data loss",
            "cost": "Low"
        },
        "active_standby": {
            "description": "Hot standby ready to take over",
            "rto": "Seconds to minutes",
            "rpo": "Near zero",
            "cost": "Medium"
        },
        "active_active": {
            "description": "Both nodes active, share load",
            "rto": "Near zero",
            "rpo": "Zero",
            "cost": "High"
        }
    }
    
    FAILOVER_AUTOMATION = """
    -- Patroni (PostgreSQL HA automation)
    -- Uses DCS (Distributed Consensus Store) like etcd
    
    -- patroni.yml:
    scope: mycluster
    name: node1
    
    restapi:
      listen: 0.0.0.0:8008
      connect_address: 10.0.0.1:8008
    
    etcd:
      hosts: 10.0.0.1:2379,10.0.0.2:2379,10.0.0.3:2379
    
    bootstrap:
      dcs:
        ttl: 30
        loop_wait: 10
        retry_timeout: 10
        maximum_lag_on_failover: 1048576
        master_start_timeout: 300
        synchronous_mode: true
        postgresql:
          use_pg_rewind: true
          parameters:
            wal_level: replica
            hot_standby: "on"
            wal_keep_size: 1GB
            max_wal_senders: 10
            max_replication_slots: 10
            wal_log_hints: "on"
    
    postgresql:
      listen: 0.0.0.0:5432
      connect_address: 10.0.0.1:5432
      data_dir: /var/lib/postgresql/data
      pgpass: /tmp/pgpass
      authentication:
        replication:
          username: replicator
          password: secret
        superuser:
          username: postgres
          password: secret
    
    -- Patroni automatically handles:
    -- - Leader election
    -- - Failover
    -- - Configuration management
    -- - Health checks
    
    -- haproxy for load balancing:
    listen postgres
      bind *:5000
      option tcp-check
      tcp-check expect rstring \\*(master|primary)\\*
      server node1 10.0.0.1:5432 check port 8008
      server node2 10.0.0.2:5432 check port 8008
      server node3 10.0.0.3:5432 check port 8008
    """


# ============== Backup & Recovery ==============

class BackupRecovery:
    """Backup strategies and disaster recovery."""
    
    STRATEGIES = {
        "full": {
            "description": "Complete database backup",
            "frequency": "Weekly",
            "retention": "4 weeks",
            "rto": "Hours",
            "rpo": "Days"
        },
        "incremental": {
            "description": "Only changes since last backup",
            "frequency": "Daily",
            "retention": "30 days",
            "rto": "Hours",
            "rpo": "Hours"
        },
        "continuous": {
            "description": "WAL archiving, point-in-time recovery",
            "frequency": "Real-time",
            "retention": "7 days",
            "rto": "Minutes",
            "rpo": "Minutes"
        },
        "snapshot": {
            "description": "Storage-level snapshots",
            "frequency": "Hourly",
            "retention": "24 hours",
            "rto": "Minutes",
            "rpo": "Hours"
        }
    }
    
    POSTGRESQL_BACKUP = """
    -- pg_dump (logical backup)
    pg_dump -h localhost -U postgres -d mydb > mydb_backup.sql
    pg_dump -h localhost -U postgres -d mydb -Fc > mydb_backup.dump  # Custom format
    pg_dump -h localhost -U postgres -d mydb -Fd -j 4 /backup/dir    # Parallel directory
    
    -- pg_restore
    pg_restore -h localhost -U postgres -d mydb mydb_backup.dump
    
    -- pg_basebackup (physical backup)
    pg_basebackup -h localhost -U replicator -D /backup/physical -Ft -z -P
    
    -- WAL archiving (for PITR)
    -- postgresql.conf:
    archive_mode = on
    archive_command = 'cp %p /backup/wal/%f'
    archive_timeout = 600
    
    -- Recovery (restore + replay WAL)
    -- recovery.conf or postgresql.conf (v12+):
    restore_command = 'cp /backup/wal/%f %p'
    recovery_target_time = '2024-01-15 14:30:00'
    recovery_target_action = 'promote'
    
    -- Automated backups with pgBackRest
    -- pgbackrest.conf:
    [global]
    repo1-path=/var/lib/pgbackrest
    repo1-retention-full=2
    repo1-retention-diff=4
    start-fast=y
    stop-auto=y
    
    [mydb]
    pg1-path=/var/lib/postgresql/data
    pg1-port=5432
    
    -- Commands:
    pgbackrest --stanza=mydb backup  # Full backup
    pgbackrest --stanza=mydb backup --type=diff  # Differential
    pgbackrest --stanza=mydb restore  # Restore
    """


# ============== Main ==============

async def main():
    """Demonstrate Phase 2 concepts."""
    print("=" * 70)
    print("DATABASE MASTERY - PHASE 2: PERFORMANCE & HIGH AVAILABILITY")
    print("=" * 70)
    
    # 1. Replication
    print("\n1. DATABASE REPLICATION")
    print("-" * 40)
    print("   Topologies:")
    for name, info in ReplicationTopologies.TOPOLOGIES.items():
        print(f"\n     {name.upper()}:")
        print(f"       Description: {info['description']}")
        print(f"       Pros: {', '.join(info['pros'][:2])}")
        print(f"       Use case: {info['use_case']}")
    
    # 2. Sharding
    print("\n2. DATABASE SHARDING")
    print("-" * 40)
    print("   Strategies:")
    for name, info in ShardingStrategies.STRATEGIES.items():
        print(f"\n     {name.upper()}:")
        print(f"       {info['description']}")
        print(f"       Example: {info['example']}")
    
    # 3. Performance Tuning
    print("\n3. PERFORMANCE TUNING")
    print("-" * 40)
    print("   Key settings:")
    settings = [
        "shared_buffers: 25% of RAM",
        "effective_cache_size: 75% of RAM",
        "work_mem: 64MB per operation",
        "random_page_cost: 1.1 for SSD",
        "max_parallel_workers: 8",
        "autovacuum: Enabled with tuned settings"
    ]
    for setting in settings:
        print(f"     • {setting}")
    
    # 4. High Availability
    print("\n4. HIGH AVAILABILITY")
    print("-" * 40)
    print("   HA Patterns:")
    for name, info in HighAvailability.PATTERNS.items():
        print(f"\n     {name.upper()}:")
        print(f"       RTO: {info['rto']}")
        print(f"       RPO: {info['rpo']}")
        print(f"       Cost: {info['cost']}")
    
    # 5. Backup & Recovery
    print("\n5. BACKUP & RECOVERY")
    print("-" * 40)
    print("   Strategies:")
    for name, info in BackupRecovery.STRATEGIES.items():
        print(f"\n     {name.upper()}:")
        print(f"       Frequency: {info['frequency']}")
        print(f"       RTO: {info['rto']}, RPO: {info['rpo']}")
    
    print("\n" + "=" * 70)
    print("PHASE 2 CONCEPTS DEMONSTRATED:")
    print("=" * 70)
    concepts = [
        "Master-Slave Replication",
        "Master-Master Replication",
        "Streaming Replication",
        "Logical Replication",
        "Hash Sharding",
        "Range Sharding",
        "Composite Sharding",
        "PostgreSQL Configuration Tuning",
        "Query Planner Hints",
        "Connection Pooling",
        "Active-Standby HA",
        "Active-Active HA",
        "Automatic Failover (Patroni)",
        "Full Backups (pg_dump)",
        "Physical Backups (pg_basebackup)",
        "Point-in-Time Recovery",
        "WAL Archiving"
    ]
    for i, concept in enumerate(concepts, 1):
        print(f"  {i:2}. {concept}")
    
    print("\n" + "=" * 70)
    print("PHASE 2 COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    asyncio.run(main())
