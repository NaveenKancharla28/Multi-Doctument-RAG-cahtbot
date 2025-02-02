#Multi-Document RAG Chatbot
This project implements a Retrieval-Augmented Generation (RAG) system for querying information from multiple documents (PDFs and CSVs). The system preprocesses, chunks, and embeds documents, stores embeddings in a FAISS index, and provides relevant document responses to user queries.

#Features
PDF and CSV Ingestion: Extracts text from PDFs and data from CSV files.
Text Chunking: Splits extracted text into smaller, manageable chunks.
Vector Embeddings: Generates embeddings for the text chunks using SentenceTransformers.
FAISS Indexing: Stores embeddings in a FAISS vector index for efficient similarity search.
Query Retrieval: Matches user queries to relevant document chunks based on semantic similarity.
Fast and Scalable: Designed for handling multiple documents and quick retrieval.


#Project Structure

multi_document_rag/
├── api/                     # Placeholder for API-related files
├── data/                    # Directory to store PDF and CSV files
├── embeddings/              # Directory for embedding files
├── models/                  # Directory for any model-related files
├── notebooks/               # Jupyter notebooks for experimentation (optional)
├── src/                     # Source code for the RAG system
│   ├── __init__.py          # Initializes and sets up the RAG system
│   ├── app.py               # Main script to run the RAG pipeline
│   ├── ingest.py            # Extracts & processes PDFs & CSVs
│   ├── chunking.py          # Splits extracted text into chunks
│   ├── embeddings.py        # Converts text chunks into vector embeddings
│   ├── retrieval.py         # Stores embeddings in FAISS & searches relevant documents
├── .gitignore               # Specifies files and folders to ignore in Git
├── README.md                # Documentation file
├── requirements.txt         # Python dependencies


#How It Works
Data Ingestion: PDFs and CSVs are processed to extract text and data.
Chunking: Text is split into smaller chunks for embedding generation.
Embedding Generation: Chunks are converted into vector embeddings using SentenceTransformers.
Storage in FAISS: Embeddings and metadata are stored in a FAISS vector index.
Query Processing: User queries are converted into embeddings, and the most similar chunks are retrieved from FAISS.
Response Generation: Retrieved chunks are returned as responses to the user query.

#Installation

#Clone the repository:
git clone https://github.com/NaveenKancharla28/Multi-Doctument-RAG-cahtbot.git
cd Multi-Doctument-RAG-cahtbot
#Install dependencies:

pip install -r requirements.txt
Usage
Add your data files (PDFs and CSVs) to the data/ directory.

#Run the RAG system:
python src/app.py
Enter a query when prompted, and the system will return relevant document chunks.

#Requirements
Python 3.7 or higher
Required Python libraries (listed in requirements.txt):
pandas
faiss
PyPDF2
sentence-transformers
Future Enhancements
Add support for more file formats (e.g., Word documents).
Implement a web-based interface for querying documents.
Optimize the FAISS index for large-scale datasets.
Integrate with GPT for generating natural language responses based on retrieved chunks.

#Contributing
Contributions are welcome! Feel free to submit issues or pull requests.
