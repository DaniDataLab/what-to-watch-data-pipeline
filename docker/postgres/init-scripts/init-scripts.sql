CREATE TABLE raw_movies (
    id SERIAL PRIMARY KEY,
    page_number INT,
    data JSONB NOT NULL,   
    source TEXT,  
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  
    file_name TEXT,                   
    file_size BIGINT,                
    movies_count INTEGER,             
    processing_status TEXT,          
    error_message TEXT           
);