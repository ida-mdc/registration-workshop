import os
import subprocess

# Directories
TEMP_DIR = "temp_repos"
DATA_DIR = "data"
CATALOGS_FILE = os.path.join(DATA_DIR, "catalogs.json")

# Create necessary directories if they don't exist
os.makedirs(DATA_DIR, exist_ok=True)


# Function to clone or update a Git repository
def clone_or_pull_repo(repo_url, repo_path):
    if os.path.isdir(repo_path):
        print(f"Pulling latest changes for {repo_path}...")
        subprocess.run(["git", "-C", repo_path, "pull"], check=True)
    else:
        print(f"Cloning repository: {repo_url}...")
        subprocess.run(["git", "clone", repo_url, repo_path], check=True)


# Function to fetch related data for a solution
def fetch_related_data(cursor, solution_id):
    # Fetch authors
    cursor.execute("""
        SELECT author.name 
        FROM solution_author 
        JOIN author ON solution_author.author_id = author.author_id
        WHERE solution_author.solution_id = ?
    """, (solution_id,))
    authors = [row[0] for row in cursor.fetchall()]

    # Fetch arguments
    cursor.execute("""
        SELECT argument.name, argument.type, argument.description, argument.default_value, argument.required
        FROM solution_argument
        JOIN argument ON solution_argument.argument_id = argument.argument_id
        WHERE solution_argument.solution_id = ?
    """, (solution_id,))
    arguments = [{"name": row[0], "type": row[1], "description": row[2], "default_value": row[3], "required": bool(row[4])} for row in cursor.fetchall()]

    # Fetch citations
    cursor.execute("""
        SELECT citation.text, citation.doi, citation.url
        FROM solution_citation
        JOIN citation ON solution_citation.citation_id = citation.citation_id
        WHERE solution_citation.solution_id = ?
    """, (solution_id,))
    citations = [{"text": row[0], "doi": row[1], "url": row[2]} for row in cursor.fetchall()]

    # Fetch documentation
    cursor.execute("""
        SELECT documentation.documentation 
        FROM documentation 
        WHERE documentation.solution_id = ?
    """, (solution_id,))
    documentation = [row[0] for row in cursor.fetchall()]

    # Fetch tags
    cursor.execute("""
        SELECT tag.name 
        FROM solution_tag
        JOIN tag ON solution_tag.tag_id = tag.tag_id
        WHERE solution_tag.solution_id = ?
    """, (solution_id,))
    tags = [row[0] for row in cursor.fetchall()]

    return {
        "authors": authors,
        "arguments": arguments,
        "citations": citations,
        "documentation": documentation,
        "tags": tags
    }


# Process each repository
os.makedirs(TEMP_DIR, exist_ok=True)


# Clean up temporary directory
subprocess.run(["rm", "-rf", TEMP_DIR])

print("All catalogs processed successfully.")
