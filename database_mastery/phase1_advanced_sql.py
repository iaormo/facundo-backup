#!/usr/bin/env python3
"""
Database Mastery - Phase 1: Advanced SQL & Database Design
Expert-level database development
"""

import sqlite3
import asyncio
from dataclasses import dataclass
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime, timedelta
from contextlib import contextmanager
import json
import re
from enum import Enum


# ============== Advanced SQL Patterns ==============

class AdvancedSQL:
    """Advanced SQL patterns and techniques."""
    
    # 1. Window Functions
    WINDOW_FUNCTIONS = """
    -- Running totals
    SELECT 
        date,
        revenue,
        SUM(revenue) OVER (ORDER BY date) as running_total,
        AVG(revenue) OVER (ORDER BY date ROWS 6 PRECEDING) as moving_avg
    FROM daily_revenue;
    
    -- Rankings
    SELECT 
        user_id,
        score,
        RANK() OVER (ORDER BY score DESC) as rank,
        DENSE_RANK() OVER (ORDER BY score DESC) as dense_rank,
        ROW_NUMBER() OVER (ORDER BY score DESC) as row_num,
        NTILE(4) OVER (ORDER BY score DESC) as quartile
    FROM user_scores;
    
    -- Partitioning
    SELECT 
        department,
        employee,
        salary,
        RANK() OVER (PARTITION BY department ORDER BY salary DESC) as dept_rank,
        salary - AVG(salary) OVER (PARTITION BY department) as diff_from_avg
    FROM employees;
    
    -- Lead/Lag for time series
    SELECT 
        date,
        revenue,
        LAG(revenue, 1) OVER (ORDER BY date) as prev_day,
        LEAD(revenue, 1) OVER (ORDER BY date) as next_day,
        revenue - LAG(revenue, 1) OVER (ORDER BY date) as day_over_day_change
    FROM daily_revenue;
    
    -- First/Last values
    SELECT 
        department,
        employee,
        salary,
        FIRST_VALUE(employee) OVER (PARTITION BY department ORDER BY salary DESC) as highest_paid,
        LAST_VALUE(employee) OVER (PARTITION BY department ORDER BY salary DESC 
                                   ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as lowest_paid
    FROM employees;
    """
    
    # 2. Common Table Expressions (CTEs)
    CTE_PATTERNS = """
    -- Recursive CTE for hierarchical data
    WITH RECURSIVE org_hierarchy AS (
        -- Anchor: top-level employees
        SELECT id, name, manager_id, 0 as level
        FROM employees
        WHERE manager_id IS NULL
        
        UNION ALL
        
        -- Recursive: employees with managers
        SELECT e.id, e.name, e.manager_id, oh.level + 1
        FROM employees e
        JOIN org_hierarchy oh ON e.manager_id = oh.id
    )
    SELECT * FROM org_hierarchy;
    
    -- Multiple CTEs
    WITH 
    monthly_stats AS (
        SELECT 
            DATE_TRUNC('month', created_at) as month,
            COUNT(*) as total_tasks,
            AVG(completion_time) as avg_completion
        FROM tasks
        GROUP BY 1
    ),
    top_performers AS (
        SELECT user_id, COUNT(*) as completed
        FROM tasks
        WHERE status = 'done'
        GROUP BY 1
        ORDER BY 2 DESC
        LIMIT 10
    )
    SELECT * FROM monthly_stats;
    
    -- Path finding with recursive CTE
    WITH RECURSIVE task_dependencies AS (
        SELECT 
            id, 
            name, 
            depends_on,
            ARRAY[id] as path,
            1 as depth
        FROM tasks
        WHERE depends_on IS NULL
        
        UNION ALL
        
        SELECT 
            t.id,
            t.name,
            t.depends_on,
            td.path || t.id,
            td.depth + 1
        FROM tasks t
        JOIN task_dependencies td ON t.depends_on = td.id
        WHERE NOT t.id = ANY(td.path)  -- Prevent cycles
    )
    SELECT * FROM task_dependencies;
    """
    
    # 3. Advanced Joins
    ADVANCED_JOINS = """
    -- Lateral join (PostgreSQL)
    SELECT u.name, top_tasks.task_name, top_tasks.priority
    FROM users u,
    LATERAL (
        SELECT name as task_name, priority
        FROM tasks
        WHERE user_id = u.id
        ORDER BY priority DESC, created_at DESC
        LIMIT 3
    ) top_tasks;
    
    -- Self join for comparisons
    SELECT 
        e1.name as employee,
        e2.name as manager,
        e1.salary as emp_salary,
        e2.salary as mgr_salary,
        e1.salary > e2.salary as earns_more_than_manager
    FROM employees e1
    LEFT JOIN employees e2 ON e1.manager_id = e2.id;
    
    -- Cross join for combinations
    SELECT d.date, p.product_name, COALESCE(s.sales, 0) as sales
    FROM generate_series('2024-01-01'::date, '2024-12-31'::date, '1 day') d
    CROSS JOIN products p
    LEFT JOIN sales s ON s.date = d.date AND s.product_id = p.id;
    
    -- Full outer join
    SELECT 
        COALESCE(a.user_id, b.user_id) as user_id,
        a.login_count,
        b.purchase_count
    FROM user_logins a
    FULL OUTER JOIN user_purchases b ON a.user_id = b.user_id;
    """


# ============== Database Design Patterns ==============

class DatabaseDesign:
    """Database design patterns and best practices."""
    
    # 1. Normalization Levels
    NORMALIZATION = {
        "1NF": "Atomic values - no repeating groups, each cell contains single value",
        "2NF": "1NF + no partial dependencies - non-key columns depend on entire primary key",
        "3NF": "2NF + no transitive dependencies - columns depend only on primary key",
        "BCNF": "3NF + every determinant is a candidate key",
        "4NF": "BCNF + no multi-valued dependencies",
        "5NF": "4NF + no join dependencies (projected tables join to original)"
    }
    
    # 2. Schema Design Examples
    SCHEMA_DESIGN = """
    -- EAV (Entity-Attribute-Value) pattern for flexible schema
    CREATE TABLE entities (
        id UUID PRIMARY KEY,
        type VARCHAR(50) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    
    CREATE TABLE attributes (
        id UUID PRIMARY KEY,
        entity_type VARCHAR(50) NOT NULL,
        attribute_name VARCHAR(100) NOT NULL,
        data_type VARCHAR(20) NOT NULL,  -- 'string', 'number', 'date', 'json'
        is_required BOOLEAN DEFAULT FALSE,
        UNIQUE(entity_type, attribute_name)
    );
    
    CREATE TABLE entity_values (
        id UUID PRIMARY KEY,
        entity_id UUID REFERENCES entities(id) ON DELETE CASCADE,
        attribute_id UUID REFERENCES attributes(id) ON DELETE CASCADE,
        string_value TEXT,
        number_value NUMERIC,
        date_value TIMESTAMP,
        json_value JSONB,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(entity_id, attribute_id)
    );
    
    -- Partitioning example (by time range)
    CREATE TABLE events (
        id BIGSERIAL,
        event_type VARCHAR(50) NOT NULL,
        user_id UUID NOT NULL,
        payload JSONB,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (id, created_at)
    ) PARTITION BY RANGE (created_at);
    
    -- Create monthly partitions
    CREATE TABLE events_2024_01 PARTITION OF events
        FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');
    CREATE TABLE events_2024_02 PARTITION OF events
        FOR VALUES FROM ('2024-02-01') TO ('2024-03-01');
    
    -- Soft deletes
    CREATE TABLE products (
        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        name VARCHAR(200) NOT NULL,
        price DECIMAL(10,2) NOT NULL,
        is_deleted BOOLEAN DEFAULT FALSE,
        deleted_at TIMESTAMP,
        deleted_by UUID REFERENCES users(id),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    
    -- Add partial index for active products only
    CREATE INDEX idx_products_active ON products(id) WHERE is_deleted = FALSE;
    
    -- Audit logging
    CREATE TABLE audit_log (
        id BIGSERIAL PRIMARY KEY,
        table_name VARCHAR(100) NOT NULL,
        record_id UUID NOT NULL,
        action VARCHAR(10) NOT NULL,  -- INSERT, UPDATE, DELETE
        old_data JSONB,
        new_data JSONB,
        changed_by UUID REFERENCES users(id),
        changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) PARTITION BY RANGE (changed_at);
    """
    
    # 3. Indexing Strategies
    INDEXING_STRATEGIES = """
    -- B-tree indexes (default, good for equality and range)
    CREATE INDEX idx_users_email ON users(email);
    CREATE INDEX idx_tasks_due_date ON tasks(due_date) WHERE status != 'done';
    
    -- Partial indexes
    CREATE INDEX idx_tasks_high_priority ON tasks(id) 
        WHERE priority = 'high' AND status = 'todo';
    
    -- Composite indexes
    CREATE INDEX idx_tasks_user_status ON tasks(user_id, status, created_at DESC);
    -- Query: WHERE user_id = ? AND status = ? ORDER BY created_at DESC
    
    -- Covering indexes (INCLUDE)
    CREATE INDEX idx_tasks_covering ON tasks(user_id, status) 
        INCLUDE (name, due_date, priority);
    -- Query can be satisfied from index alone
    
    -- GIN indexes for JSON/arrays
    CREATE INDEX idx_tasks_tags ON tasks USING GIN(tags);
    CREATE INDEX idx_events_payload ON events USING GIN(payload);
    
    -- GiST indexes for geometric/text search
    CREATE INDEX idx_locations_coords ON locations USING GiST(
        ll_to_earth(latitude, longitude)
    );
    
    -- BRIN indexes for large, naturally ordered tables
    CREATE INDEX idx_events_created_brin ON events USING BRIN(created_at);
    -- Good for time-series data where values correlate with physical order
    
    -- Expression indexes
    CREATE INDEX idx_users_email_lower ON users(LOWER(email));
    -- Query: WHERE LOWER(email) = LOWER(?)
    
    CREATE INDEX idx_tasks_name_trgm ON tasks USING GIN(name gin_trgm_ops);
    -- For fuzzy text search with pg_trgm
    """


# ============== Query Optimization ==============

class QueryOptimization:
    """Query optimization techniques."""
    
    # 1. Execution Plan Analysis
    EXPLAIN_ANALYZE = """
    -- Basic EXPLAIN
    EXPLAIN SELECT * FROM tasks WHERE user_id = 'abc' AND status = 'todo';
    
    -- Detailed analysis
    EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)
    SELECT t.*, u.name as assignee
    FROM tasks t
    JOIN users u ON t.user_id = u.id
    WHERE t.status = 'doing'
    ORDER BY t.priority DESC, t.created_at DESC
    LIMIT 20;
    
    -- Key metrics to check:
    -- - Seq Scan vs Index Scan
    -- - Rows estimated vs actual
    -- - Buffer hits vs reads
    -- - Execution time
    """
    
    # 2. Optimization Techniques
    OPTIMIZATION_TECHNIQUES = """
    -- 1. Select only needed columns
    -- BAD: SELECT * FROM large_table
    -- GOOD: SELECT id, name FROM large_table
    
    -- 2. Use appropriate indexes
    CREATE INDEX CONCURRENTLY idx_large_table_filter ON large_table(filter_col);
    -- Use CONCURRENTLY to avoid locking in production
    
    -- 3. Batch processing for large updates
    -- BAD: UPDATE huge_table SET status = 'archived' WHERE created_at < '2023-01-01'
    -- GOOD: Process in batches
    DO $$
    DECLARE
        batch_size INT := 1000;
        rows_updated INT;
    BEGIN
        LOOP
            UPDATE huge_table 
            SET status = 'archived'
            WHERE id IN (
                SELECT id FROM huge_table
                WHERE created_at < '2023-01-01' AND status != 'archived'
                LIMIT batch_size
            );
            GET DIAGNOSTICS rows_updated = ROW_COUNT;
            EXIT WHEN rows_updated = 0;
            COMMIT;
        END LOOP;
    END $$;
    
    -- 4. Avoid N+1 queries
    -- BAD: Loop through users, query tasks for each
    -- GOOD: Single query with JOIN or IN
    SELECT u.*, json_agg(t.*) as tasks
    FROM users u
    LEFT JOIN tasks t ON u.id = t.user_id
    WHERE u.id IN (SELECT user_id FROM active_users)
    GROUP BY u.id;
    
    -- 5. Use EXISTS for semi-joins
    -- Better than IN for large subqueries
    SELECT * FROM orders o
    WHERE EXISTS (
        SELECT 1 FROM order_items oi
        WHERE oi.order_id = o.id AND oi.price > 1000
    );
    
    -- 6. Pagination with keyset pagination for large offsets
    -- BAD: OFFSET 100000 (slow, reads all rows)
    -- GOOD: Keyset pagination
    SELECT * FROM tasks
    WHERE (created_at, id) < (last_seen_date, last_seen_id)
    ORDER BY created_at DESC, id DESC
    LIMIT 20;
    """
    
    # 3. Materialized Views
    MATERIALIZED_VIEWS = """
    -- Create materialized view for expensive aggregations
    CREATE MATERIALIZED VIEW daily_task_stats AS
    SELECT 
        DATE(created_at) as date,
        status,
        priority,
        COUNT(*) as task_count,
        AVG(EXTRACT(EPOCH FROM (completed_at - created_at))/3600) as avg_hours_to_complete
    FROM tasks
    GROUP BY 1, 2, 3;
    
    -- Index the materialized view
    CREATE INDEX idx_daily_stats_date ON daily_task_stats(date);
    
    -- Refresh strategies:
    -- 1. Manual refresh
    REFRESH MATERIALIZED VIEW daily_task_stats;
    
    -- 2. Concurrent refresh (no locks)
    REFRESH MATERIALIZED VIEW CONCURRENTLY daily_task_stats;
    
    -- 3. Scheduled refresh with pg_cron
    SELECT cron.schedule('refresh-stats', '0 1 * * *', 
        'REFRESH MATERIALIZED VIEW CONCURRENTLY daily_task_stats');
    
    -- 4. Trigger-based refresh
    CREATE OR REPLACE FUNCTION refresh_task_stats()
    RETURNS TRIGGER AS $$
    BEGIN
        PERFORM pg_notify('refresh_stats', 'tasks_updated');
        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
    """


# ============== Transaction Management ==============

class TransactionManagement:
    """Advanced transaction handling."""
    
    ISOLATION_LEVELS = {
        "READ UNCOMMITTED": "Dirty reads allowed (rarely used)",
        "READ COMMITTED": "Default. No dirty reads, non-repeatable reads possible",
        "REPEATABLE READ": "Snapshot at transaction start. Phantom reads possible",
        "SERIALIZABLE": "Full isolation. Slowest but safest"
    }
    
    PATTERNS = """
    -- Optimistic locking with version column
    CREATE TABLE inventory (
        id UUID PRIMARY KEY,
        product_name VARCHAR(100),
        quantity INTEGER NOT NULL,
        version INTEGER DEFAULT 1
    );
    
    -- Update with version check
    UPDATE inventory 
    SET quantity = quantity - 1, version = version + 1
    WHERE id = 'product-123' AND version = 5;
    -- Check rows affected = 1, otherwise retry
    
    -- Advisory locks for application-level locking
    SELECT pg_advisory_lock(hashtext('task-processing'));
    -- Do work
    SELECT pg_advisory_unlock(hashtext('task-processing'));
    
    -- Skip locked rows (for queue processing)
    SELECT * FROM task_queue
    WHERE status = 'pending'
    ORDER BY created_at
    FOR UPDATE SKIP LOCKED
    LIMIT 1;
    
    -- Savepoints for partial rollback
    BEGIN;
    INSERT INTO users (name) VALUES ('Alice');
    SAVEPOINT before_payment;
    
    -- Try risky operation
    INSERT INTO payments (amount) VALUES (1000);
    
    -- If it fails:
    ROLLBACK TO SAVEPOINT before_payment;
    
    COMMIT;
    
    -- Two-phase commit (distributed transactions)
    -- Prepare transaction
    PREPARE TRANSACTION 'txn-123';
    -- On all nodes, then:
    COMMIT PREPARED 'txn-123';
    -- Or: ROLLBACK PREPARED 'txn-123';
    """


# ============== Database Migration Patterns ==============

MIGRATION_STRATEGIES = """
-- Zero-downtime migration patterns

-- 1. Expand-contract pattern
-- Step 1: Add new column (nullable)
ALTER TABLE users ADD COLUMN email_normalized VARCHAR(255);

-- Step 2: Backfill in batches
UPDATE users 
SET email_normalized = LOWER(email)
WHERE id IN (SELECT id FROM users WHERE email_normalized IS NULL LIMIT 1000);

-- Step 3: Add trigger for new writes
CREATE TRIGGER normalize_email
    BEFORE INSERT OR UPDATE ON users
    FOR EACH ROW
    EXECUTE FUNCTION normalize_email_trigger();

-- Step 4: Make column NOT NULL once backfilled
ALTER TABLE users ALTER COLUMN email_normalized SET NOT NULL;

-- Step 5: Add index
CREATE INDEX CONCURRENTLY idx_users_email_norm ON users(email_normalized);

-- Step 6: Update application to use new column

-- Step 7: Drop old column
ALTER TABLE users DROP COLUMN email;


-- 2. Blue-green deployment
-- - Create new schema/schema version
-- - Dual-write to both schemas
-- - Backfill historical data
-- - Switch reads to new schema
-- - Stop writes to old schema
-- - Drop old schema


-- 3. Shadow writes
-- - Write to both old and new tables
-- - Read from old table
-- - Verify consistency
-- - Switch reads to new table
-- - Stop writes to old table
-- - Drop old table


-- Migration safety checklist:
-- [ ] Use transactions for schema changes
-- [ ] Add CONCURRENTLY to CREATE INDEX
-- [ ] Backfill in batches
-- [ ] Have rollback plan
-- [ ] Test on copy of production data
-- [ ] Monitor during migration
"""


# ============== Demo Database Setup ==============

class DemoDatabase:
    """Setup demo database with sample data."""
    
    def __init__(self, db_path: str = ":memory:"):
        self.db_path = db_path
        self.conn = None
    
    def setup(self):
        """Create schema and sample data."""
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        
        # Create tables
        self.conn.executescript("""
            CREATE TABLE users (
                id TEXT PRIMARY KEY,
                email TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                department TEXT,
                salary INTEGER,
                manager_id TEXT,
                created_at TEXT
            );
            
            CREATE TABLE tasks (
                id TEXT PRIMARY KEY,
                user_id TEXT,
                name TEXT NOT NULL,
                status TEXT DEFAULT 'todo',
                priority TEXT DEFAULT 'medium',
                due_date TEXT,
                created_at TEXT,
                completed_at TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );
            
            CREATE TABLE projects (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                budget INTEGER,
                start_date TEXT,
                end_date TEXT
            );
            
            CREATE TABLE employee_projects (
                employee_id TEXT,
                project_id TEXT,
                role TEXT,
                hours_allocated INTEGER,
                PRIMARY KEY (employee_id, project_id)
            );
        """)
        
        # Insert sample data
        self._insert_sample_data()
        self.conn.commit()
        return self
    
    def _insert_sample_data(self):
        """Insert sample data."""
        users = [
            ('u1', 'alice@scaleplus.io', 'Alice Johnson', 'Engineering', 120000, None, '2023-01-15'),
            ('u2', 'bob@scaleplus.io', 'Bob Smith', 'Engineering', 95000, 'u1', '2023-02-01'),
            ('u3', 'carol@scaleplus.io', 'Carol White', 'Design', 85000, 'u1', '2023-02-15'),
            ('u4', 'david@scaleplus.io', 'David Brown', 'Marketing', 75000, 'u1', '2023-03-01'),
            ('u5', 'eve@scaleplus.io', 'Eve Davis', 'Engineering', 110000, 'u2', '2023-04-01'),
        ]
        
        tasks = [
            ('t1', 'u1', 'Design system architecture', 'done', 'high', '2024-01-15', '2023-12-01', '2024-01-10'),
            ('t2', 'u1', 'Review pull requests', 'doing', 'medium', '2024-02-01', '2024-01-20', None),
            ('t3', 'u2', 'Implement API endpoints', 'done', 'high', '2024-01-30', '2024-01-05', '2024-01-25'),
            ('t4', 'u2', 'Write unit tests', 'todo', 'high', '2024-02-10', '2024-01-25', None),
            ('t5', 'u3', 'Create UI mockups', 'done', 'medium', '2024-01-20', '2024-01-10', '2024-01-18'),
            ('t6', 'u4', 'Prepare marketing campaign', 'doing', 'low', '2024-02-15', '2024-01-15', None),
            ('t7', 'u5', 'Optimize database queries', 'todo', 'high', '2024-02-05', '2024-01-28', None),
        ]
        
        projects = [
            ('p1', 'Website Redesign', 50000, '2024-01-01', '2024-03-31'),
            ('p2', 'Mobile App', 100000, '2024-02-01', '2024-06-30'),
            ('p3', 'Analytics Dashboard', 30000, '2024-01-15', '2024-04-30'),
        ]
        
        emp_projects = [
            ('u1', 'p1', 'Tech Lead', 20),
            ('u2', 'p1', 'Developer', 40),
            ('u3', 'p1', 'Designer', 30),
            ('u1', 'p2', 'Architect', 10),
            ('u5', 'p2', 'Developer', 40),
            ('u4', 'p3', 'Product Owner', 15),
        ]
        
        self.conn.executemany(
            "INSERT INTO users VALUES (?,?,?,?,?,?,?)", users
        )
        self.conn.executemany(
            "INSERT INTO tasks VALUES (?,?,?,?,?,?,?,?)", tasks
        )
        self.conn.executemany(
            "INSERT INTO projects VALUES (?,?,?,?,?)", projects
        )
        self.conn.executemany(
            "INSERT INTO employee_projects VALUES (?,?,?,?)", emp_projects
        )
    
    def query(self, sql: str, params: tuple = ()) -> List[Dict]:
        """Execute query and return results."""
        cursor = self.conn.execute(sql, params)
        return [dict(row) for row in cursor.fetchall()]
    
    def close(self):
        """Close connection."""
        if self.conn:
            self.conn.close()


# ============== Main ==============

async def main():
    """Demonstrate database mastery concepts."""
    print("=" * 70)
    print("DATABASE MASTERY - PHASE 1: ADVANCED SQL & DATABASE DESIGN")
    print("=" * 70)
    
    # Setup demo database
    db = DemoDatabase().setup()
    
    # 1. Complex Queries
    print("\n1. COMPLEX QUERIES")
    print("-" * 40)
    
    # Join with aggregation
    print("   Task completion by department:")
    results = db.query("""
        SELECT 
            u.department,
            COUNT(t.id) as total_tasks,
            SUM(CASE WHEN t.status = 'done' THEN 1 ELSE 0 END) as completed,
            ROUND(AVG(CASE WHEN t.status = 'done' 
                THEN (julianday(t.completed_at) - julianday(t.created_at))
                ELSE NULL END), 2) as avg_days_to_complete
        FROM users u
        LEFT JOIN tasks t ON u.id = t.user_id
        GROUP BY u.department
        ORDER BY total_tasks DESC
    """)
    for row in results:
        print(f"     {row['department']}: {row['completed']}/{row['total_tasks']} tasks, avg {row['avg_days_to_complete']} days")
    
    # Recursive CTE simulation (SQLite doesn't have true recursion)
    print("\n   Employee hierarchy (manager relationships):")
    results = db.query("""
        SELECT 
            e.name as employee,
            e.department,
            e.salary,
            m.name as manager,
            m.salary as manager_salary
        FROM users e
        LEFT JOIN users m ON e.manager_id = m.id
        ORDER BY m.name NULLS FIRST, e.salary DESC
    """)
    for row in results:
        mgr = row['manager'] or 'CEO'
        print(f"     {row['employee']} ({row['department']}) - Manager: {mgr}")
    
    # Window functions simulation
    print("\n   Task priorities ranked by user:")
    results = db.query("""
        SELECT 
            u.name,
            t.name as task_name,
            t.priority,
            t.status,
            ROW_NUMBER() OVER (PARTITION BY u.id ORDER BY 
                CASE t.priority 
                    WHEN 'high' THEN 1 
                    WHEN 'medium' THEN 2 
                    ELSE 3 
                END
            ) as priority_rank
        FROM users u
        JOIN tasks t ON u.id = t.user_id
        WHERE t.status != 'done'
        ORDER BY u.name, priority_rank
    """)
    for row in results:
        print(f"     {row['name']}: {row['task_name']} ({row['priority']})")
    
    # 2. Database Design
    print("\n2. DATABASE DESIGN PATTERNS")
    print("-" * 40)
    print("   Normalization levels:")
    for level, desc in DatabaseDesign.NORMALIZATION.items():
        print(f"     {level}: {desc[:50]}...")
    
    print("\n   Indexing strategies:")
    strategies = [
        "B-tree indexes for equality and range queries",
        "Partial indexes for filtered queries",
        "Composite indexes for multi-column lookups",
        "Covering indexes to avoid table access",
        "GIN indexes for JSON and array data",
        "BRIN indexes for large time-series tables"
    ]
    for strategy in strategies:
        print(f"     • {strategy}")
    
    # 3. Query Optimization
    print("\n3. QUERY OPTIMIZATION")
    print("-" * 40)
    print("   Key techniques:")
    techniques = [
        "Select only needed columns",
        "Use appropriate indexes (CONCURRENTLY in production)",
        "Batch large updates (avoid long transactions)",
        "Avoid N+1 queries (use JOINs)",
        "Use EXISTS for semi-joins",
        "Keyset pagination for large offsets",
        "Materialized views for expensive aggregations"
    ]
    for technique in techniques:
        print(f"     • {technique}")
    
    # 4. Transaction Management
    print("\n4. TRANSACTION MANAGEMENT")
    print("-" * 40)
    print("   Isolation levels:")
    for level, desc in TransactionManagement.ISOLATION_LEVELS.items():
        print(f"     {level}: {desc}")
    
    # 5. Migration Patterns
    print("\n5. MIGRATION STRATEGIES")
    print("-" * 40)
    strategies = [
        "Expand-contract pattern for schema changes",
        "Blue-green deployment for zero downtime",
        "Shadow writes for data migration",
        "Advisory locks for application-level locking",
        "Optimistic locking with version columns"
    ]
    for strategy in strategies:
        print(f"     • {strategy}")
    
    db.close()
    
    print("\n" + "=" * 70)
    print("PHASE 1 CONCEPTS DEMONSTRATED:")
    print("=" * 70)
    concepts = [
        "Advanced SQL (Window Functions)",
        "Common Table Expressions (CTEs)",
        "Recursive Queries",
        "Complex Joins (Lateral, Self, Cross)",
        "Database Normalization (1NF-5NF)",
        "Schema Design Patterns",
        "EAV (Entity-Attribute-Value)",
        "Table Partitioning",
        "Soft Deletes",
        "Audit Logging",
        "Indexing Strategies",
        "Query Optimization",
        "Materialized Views",
        "Transaction Isolation Levels",
        "Zero-downtime Migrations",
        "Locking Patterns"
    ]
    for i, concept in enumerate(concepts, 1):
        print(f"  {i:2}. {concept}")
    
    print("\n" + "=" * 70)
    print("PHASE 1 COMPLETE")
    print("=" * 70)
    print("\nReady for Phase 2: Performance Tuning & High Availability")


if __name__ == "__main__":
    asyncio.run(main())
