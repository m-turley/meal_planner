CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    recipe_name VARCHAR(255) NOT NULL,
    recipe_link VARCHAR(2048) NOT NULL
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    tag_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE recipe_tags (
    recipe_id INT NOT NULL,
    tag_id INT NOT NULL,
    PRIMARY KEY (recipe_id, tag_id),
    CONSTRAINT fk_recipe
        FOREIGN KEY (recipe_id) 
        REFERENCES recipes(id) 
        ON DELETE CASCADE,
    CONSTRAINT fk_tag
        FOREIGN KEY (tag_id) 
        REFERENCES tags(id) 
        ON DELETE CASCADE
);