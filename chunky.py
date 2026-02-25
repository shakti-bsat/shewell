from langchain_text_splitters import RecursiveCharacterTextSplitter



def chunk(data, chunky_size =1000, chunk_overlap=150):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    documents = []

    for item in data:
        chunks = text_splitter.split_text(item["content"])
        
        for chunk in chunks:
            documents.append({
                "text": chunk,
                "source": item["url"],
                "title": item["title"]
            })
    return documents