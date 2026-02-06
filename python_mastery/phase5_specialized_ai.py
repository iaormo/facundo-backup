#!/usr/bin/env python3
"""
Phase 5: Specialized AI
NLP, Computer Vision, Advanced RAG, Data Engineering
"""

import asyncio
import json
import re
import math
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple, Set
from collections import defaultdict, Counter


# ============== NLP (Natural Language Processing) ==============

class Tokenizer:
    """Text tokenization with multiple strategies."""
    
    @staticmethod
    def word_tokenize(text: str) -> List[str]:
        """Simple word tokenization."""
        return re.findall(r'\b\w+\b', text.lower())
    
    @staticmethod
    def sentence_tokenize(text: str) -> List[str]:
        """Sentence tokenization."""
        sentences = re.split(r'(?<=[.!?])\s+', text)
        return [s.strip() for s in sentences if s.strip()]
    
    @staticmethod
    def ngrams(tokens: List[str], n: int) -> List[Tuple[str, ...]]:
        """Generate n-grams from tokens."""
        return [tuple(tokens[i:i+n]) for i in range(len(tokens) - n + 1)]


class TextPreprocessor:
    """Text preprocessing pipeline."""
    
    def __init__(self):
        self.stopwords: Set[str] = {
            'the', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been',
            'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will',
            'would', 'could', 'should', 'may', 'might', 'must', 'shall',
            'can', 'need', 'dare', 'ought', 'used', 'to', 'of', 'in',
            'for', 'on', 'with', 'at', 'by', 'from', 'as', 'into',
            'through', 'during', 'before', 'after', 'above', 'below',
            'between', 'under', 'and', 'but', 'or', 'yet', 'so'
        }
    
    def remove_stopwords(self, tokens: List[str]) -> List[str]:
        """Remove common stopwords."""
        return [t for t in tokens if t not in self.stopwords]
    
    def remove_punctuation(self, text: str) -> str:
        """Remove punctuation."""
        return re.sub(r'[^\w\s]', '', text)
    
    def stem(self, word: str) -> str:
        """Simple Porter-style stemming."""
        # Simplified stemming rules
        suffixes = ['ing', 'ly', 'ed', 'ies', 'ied', 'ies', 'ied', 's']
        for suffix in suffixes:
            if word.endswith(suffix):
                return word[:-len(suffix)]
        return word
    
    def preprocess(self, text: str) -> List[str]:
        """Full preprocessing pipeline."""
        text = self.remove_punctuation(text)
        tokens = Tokenizer.word_tokenize(text)
        tokens = self.remove_stopwords(tokens)
        tokens = [self.stem(t) for t in tokens]
        return tokens


class TFIDF:
    """TF-IDF vectorization for text."""
    
    def __init__(self):
        self.documents: List[List[str]] = []
        self.idf: Dict[str, float] = {}
        self.vocab: Set[str] = set()
    
    def fit(self, documents: List[str]):
        """Calculate IDF scores."""
        preprocessor = TextPreprocessor()
        self.documents = [preprocessor.preprocess(doc) for doc in documents]
        
        # Build vocabulary
        for doc in self.documents:
            self.vocab.update(doc)
        
        # Calculate IDF
        n_docs = len(self.documents)
        for term in self.vocab:
            doc_count = sum(1 for doc in self.documents if term in doc)
            self.idf[term] = math.log(n_docs / (doc_count + 1)) + 1
    
    def transform(self, document: str) -> Dict[str, float]:
        """Transform document to TF-IDF vector."""
        preprocessor = TextPreprocessor()
        tokens = preprocessor.preprocess(document)
        
        # Calculate term frequency
        tf = Counter(tokens)
        total_terms = len(tokens)
        
        # Calculate TF-IDF
        vector = {}
        for term, freq in tf.items():
            if term in self.idf:
                tf_score = freq / total_terms
                vector[term] = tf_score * self.idf[term]
        
        return vector
    
    def fit_transform(self, documents: List[str]) -> List[Dict[str, float]]:
        """Fit and transform documents."""
        self.fit(documents)
        return [self.transform(doc) for doc in documents]


class NamedEntityRecognizer:
    """Simple rule-based NER."""
    
    PATTERNS = {
        'PERSON': [
            r'\b[A-Z][a-z]+ [A-Z][a-z]+\b',  # First Last
            r'\b(Mr|Mrs|Ms|Dr)\.? [A-Z][a-z]+\b'
        ],
        'ORGANIZATION': [
            r'\b[A-Z][a-z]* (Inc|Corp|LLC|Ltd|Company)\b',
            r'\b(ScalePlus|Hayahaya|Victory|Notion|Discord)\b'
        ],
        'DATE': [
            r'\b\d{1,2}/\d{1,2}/\d{2,4}\b',
            r'\b(January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}\b',
            r'\btomorrow\b|\btoday\b|\byesterday\b'
        ],
        'MONEY': [
            r'\$\d+(?:,\d{3})*(?:\.\d{2})?',
            r'\b\d+(?:,\d{3})* (PHP|USD|EUR)\b'
        ]
    }
    
    def extract(self, text: str) -> List[Dict[str, str]]:
        """Extract named entities."""
        entities = []
        for entity_type, patterns in self.PATTERNS.items():
            for pattern in patterns:
                for match in re.finditer(pattern, text, re.IGNORECASE):
                    entities.append({
                        'text': match.group(),
                        'type': entity_type,
                        'start': match.start(),
                        'end': match.end()
                    })
        return sorted(entities, key=lambda x: x['start'])


class SentimentAnalyzer:
    """Simple lexicon-based sentiment analysis."""
    
    POSITIVE_WORDS = {
        'good', 'great', 'excellent', 'amazing', 'awesome', 'fantastic',
        'wonderful', 'perfect', 'love', 'best', 'happy', 'excited',
        'successful', 'profitable', 'efficient', 'smooth'
    }
    
    NEGATIVE_WORDS = {
        'bad', 'terrible', 'awful', 'horrible', 'worst', 'hate',
        'angry', 'frustrated', 'disappointed', 'failed', 'broken',
        'buggy', 'slow', 'expensive', 'difficult'
    }
    
    INTENSIFIERS = {
        'very': 1.5, 'extremely': 2.0, 'really': 1.3,
        'quite': 1.2, 'somewhat': 0.8, 'slightly': 0.5
    }
    
    def analyze(self, text: str) -> Dict[str, Any]:
        """Analyze sentiment of text."""
        tokens = Tokenizer.word_tokenize(text.lower())
        
        score = 0
        details = {'positive': [], 'negative': []}
        
        i = 0
        while i < len(tokens):
            token = tokens[i]
            intensity = 1.0
            
            # Check for intensifier
            if i > 0 and tokens[i-1] in self.INTENSIFIERS:
                intensity = self.INTENSIFIERS[tokens[i-1]]
            
            if token in self.POSITIVE_WORDS:
                score += intensity
                details['positive'].append(token)
            elif token in self.NEGATIVE_WORDS:
                score -= intensity
                details['negative'].append(token)
            
            i += 1
        
        # Normalize
        if len(tokens) > 0:
            normalized_score = score / math.sqrt(len(tokens))
        else:
            normalized_score = 0
        
        # Determine sentiment
        if normalized_score > 0.1:
            sentiment = 'positive'
        elif normalized_score < -0.1:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        
        return {
            'sentiment': sentiment,
            'score': round(normalized_score, 3),
            'confidence': min(abs(normalized_score) * 2, 1.0),
            'details': details
        }


# ============== Computer Vision ==============

@dataclass
class Image:
    """Simple image representation."""
    width: int
    height: int
    pixels: List[List[Tuple[int, int, int]]]  # RGB tuples
    
    def get_pixel(self, x: int, y: int) -> Tuple[int, int, int]:
        """Get pixel at coordinates."""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.pixels[y][x]
        return (0, 0, 0)
    
    def set_pixel(self, x: int, y: int, color: Tuple[int, int, int]):
        """Set pixel at coordinates."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.pixels[y][x] = color


class ImageProcessor:
    """Image processing operations."""
    
    @staticmethod
    def grayscale(image: Image) -> Image:
        """Convert image to grayscale."""
        new_pixels = []
        for row in image.pixels:
            new_row = []
            for r, g, b in row:
                # Luminance formula
                gray = int(0.299 * r + 0.587 * g + 0.114 * b)
                new_row.append((gray, gray, gray))
            new_pixels.append(new_row)
        return Image(image.width, image.height, new_pixels)
    
    @staticmethod
    def blur(image: Image, radius: int = 1) -> Image:
        """Simple box blur."""
        new_pixels = []
        for y in range(image.height):
            row = []
            for x in range(image.width):
                # Average surrounding pixels
                r_sum, g_sum, b_sum, count = 0, 0, 0, 0
                for dy in range(-radius, radius + 1):
                    for dx in range(-radius, radius + 1):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < image.width and 0 <= ny < image.height:
                            r, g, b = image.get_pixel(nx, ny)
                            r_sum += r
                            g_sum += g
                            b_sum += b
                            count += 1
                row.append((r_sum // count, g_sum // count, b_sum // count))
            new_pixels.append(row)
        return Image(image.width, image.height, new_pixels)
    
    @staticmethod
    def edge_detect(image: Image) -> Image:
        """Sobel edge detection."""
        new_pixels = []
        for y in range(1, image.height - 1):
            row = []
            for x in range(1, image.width - 1):
                # Sobel operators
                gx = (
                    -1 * sum(image.get_pixel(x-1, y-1)) +
                     1 * sum(image.get_pixel(x+1, y-1)) +
                    -2 * sum(image.get_pixel(x-1, y)) +
                     2 * sum(image.get_pixel(x+1, y)) +
                    -1 * sum(image.get_pixel(x-1, y+1)) +
                     1 * sum(image.get_pixel(x+1, y+1))
                ) / 9
                
                gy = (
                    -1 * sum(image.get_pixel(x-1, y-1)) +
                    -2 * sum(image.get_pixel(x, y-1)) +
                    -1 * sum(image.get_pixel(x+1, y-1)) +
                     1 * sum(image.get_pixel(x-1, y+1)) +
                     2 * sum(image.get_pixel(x, y+1)) +
                     1 * sum(image.get_pixel(x+1, y+1))
                ) / 9
                
                magnitude = int(min(255, math.sqrt(gx**2 + gy**2)))
                row.append((magnitude, magnitude, magnitude))
            
            # Pad row
            row = [(0, 0, 0)] + row + [(0, 0, 0)]
            new_pixels.append(row)
        
        # Pad top and bottom
        padding = [(0, 0, 0)] * image.width
        new_pixels = [padding] + new_pixels + [padding]
        
        return Image(image.width, image.height, new_pixels)


class OCR:
    """Simple OCR concepts (demonstration)."""
    
    @staticmethod
    def extract_text(image: Image) -> str:
        """Mock OCR - would use Tesseract in production."""
        # This is a placeholder - real OCR uses ML models
        return "[OCR: Text extraction would use Tesseract or similar]"
    
    @staticmethod
    def preprocess_for_ocr(image: Image) -> Image:
        """Preprocess image for better OCR."""
        # 1. Convert to grayscale
        gray = ImageProcessor.grayscale(image)
        # 2. Apply thresholding (simplified)
        # 3. Remove noise
        return gray


# ============== Data Engineering ==============

class ETLPipeline:
    """Extract, Transform, Load pipeline."""
    
    def __init__(self):
        self.extractors: List[callable] = []
        self.transformers: List[callable] = []
        self.loaders: List[callable] = []
    
    def add_extractor(self, extractor: callable):
        """Add extraction step."""
        self.extractors.append(extractor)
    
    def add_transformer(self, transformer: callable):
        """Add transformation step."""
        self.transformers.append(transformer)
    
    def add_loader(self, loader: callable):
        """Add loading step."""
        self.loaders.append(loader)
    
    async def run(self, source: Any) -> Any:
        """Run full ETL pipeline."""
        # Extract
        data = source
        for extractor in self.extractors:
            data = await extractor(data)
        
        # Transform
        for transformer in self.transformers:
            data = await transformer(data)
        
        # Load
        for loader in self.loaders:
            data = await loader(data)
        
        return data


class DataValidator:
    """Data validation with Pydantic-style patterns."""
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email format."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def validate_phone(phone: str) -> bool:
        """Validate phone number."""
        digits = re.sub(r'\D', '', phone)
        return 10 <= len(digits) <= 15
    
    @staticmethod
    def validate_json(data: str) -> Optional[Dict]:
        """Validate and parse JSON."""
        try:
            return json.loads(data)
        except json.JSONDecodeError:
            return None


# ============== Advanced RAG ==============

class Chunker:
    """Text chunking strategies."""
    
    @staticmethod
    def fixed_size(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
        """Fixed-size chunking with overlap."""
        chunks = []
        start = 0
        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]
            chunks.append(chunk)
            start = end - overlap
        return chunks
    
    @staticmethod
    def semantic(text: str, sentences_per_chunk: int = 3) -> List[str]:
        """Semantic chunking by sentences."""
        sentences = Tokenizer.sentence_tokenize(text)
        chunks = []
        for i in range(0, len(sentences), sentences_per_chunk):
            chunk = ' '.join(sentences[i:i+sentences_per_chunk])
            chunks.append(chunk)
        return chunks


class QueryExpander:
    """Expand queries for better retrieval."""
    
    def __init__(self):
        self.synonyms = {
            'website': ['site', 'webpage', 'landing page'],
            'price': ['cost', 'fee', 'rate', 'pricing'],
            'task': ['todo', 'action item', 'work item'],
            'business': ['company', 'enterprise', 'organization']
        }
    
    def expand(self, query: str) -> List[str]:
        """Generate query variations."""
        variations = [query]
        tokens = Tokenizer.word_tokenize(query.lower())
        
        for token in tokens:
            if token in self.synonyms:
                for synonym in self.synonyms[token]:
                    new_query = query.replace(token, synonym)
                    variations.append(new_query)
        
        return variations


class ReRanker:
    """Re-rank retrieval results."""
    
    def rerank(self, query: str, results: List[Dict], top_k: int = 5) -> List[Dict]:
        """Re-rank results based on query relevance."""
        query_tokens = set(Tokenizer.word_tokenize(query.lower()))
        
        scored_results = []
        for result in results:
            content = result.get('content', '')
            content_tokens = set(Tokenizer.word_tokenize(content.lower()))
            
            # Calculate overlap
            overlap = len(query_tokens & content_tokens)
            score = overlap / max(len(query_tokens), 1)
            
            scored_results.append({**result, 'score': score})
        
        # Sort by score
        scored_results.sort(key=lambda x: x['score'], reverse=True)
        return scored_results[:top_k]


# ============== Main ==============

async def main():
    """Demonstrate Phase 5 specialized AI."""
    print("=" * 70)
    print("PHASE 5: SPECIALIZED AI")
    print("=" * 70)
    
    # 1. NLP - Tokenization
    print("\n1. NLP - TOKENIZATION")
    print("-" * 40)
    
    text = "ScalePlus.io builds websites. Hayahaya rents adventure gear. Both are great businesses!"
    tokens = Tokenizer.word_tokenize(text)
    sentences = Tokenizer.sentence_tokenize(text)
    bigrams = Tokenizer.ngrams(tokens, 2)
    
    print(f"   Text: {text[:50]}...")
    print(f"   Tokens: {tokens[:10]}")
    print(f"   Sentences: {len(sentences)}")
    print(f"   Bigrams: {list(bigrams)[:5]}")
    
    # 2. NLP - Preprocessing
    print("\n2. NLP - TEXT PREPROCESSING")
    print("-" * 40)
    
    preprocessor = TextPreprocessor()
    processed = preprocessor.preprocess(text)
    print(f"   Original: {text[:50]}...")
    print(f"   Processed: {processed[:10]}")
    
    # 3. NLP - TF-IDF
    print("\n3. NLP - TF-IDF VECTORIZATION")
    print("-" * 40)
    
    documents = [
        "ScalePlus builds websites for small businesses",
        "Hayahaya rents Jimny and camping gear",
        "Website pricing starts at 4995 pesos monthly",
        "Jimny rental costs 3500 pesos per day"
    ]
    
    tfidf = TFIDF()
    vectors = tfidf.fit_transform(documents)
    
    print(f"   Documents: {len(documents)}")
    print(f"   Vocabulary size: {len(tfidf.vocab)}")
    print(f"   Sample TF-IDF (doc 1): {dict(list(vectors[0].items())[:3])}")
    
    # 4. NLP - Named Entity Recognition
    print("\n4. NLP - NAMED ENTITY RECOGNITION")
    print("-" * 40)
    
    ner = NamedEntityRecognizer()
    sample_text = "ScalePlus.io charges 4995 PHP per month. Contact Mr. Ian by January 15."
    entities = ner.extract(sample_text)
    
    print(f"   Text: {sample_text}")
    print("   Entities found:")
    for entity in entities:
        print(f"     - {entity['text']} ({entity['type']})")
    
    # 5. NLP - Sentiment Analysis
    print("\n5. NLP - SENTIMENT ANALYSIS")
    print("-" * 40)
    
    sentiment = SentimentAnalyzer()
    reviews = [
        "The service was excellent and very efficient!",
        "Terrible experience, very disappointed",
        "The website works fine, nothing special"
    ]
    
    for review in reviews:
        result = sentiment.analyze(review)
        print(f"   '{review[:40]}...' → {result['sentiment']} ({result['score']})")
    
    # 6. Computer Vision
    print("\n6. COMPUTER VISION")
    print("-" * 40)
    
    # Create sample image
    pixels = [[(i*10, j*10, (i+j)*5) for i in range(10)] for j in range(10)]
    image = Image(10, 10, pixels)
    
    print(f"   Created image: {image.width}x{image.height}")
    
    gray = ImageProcessor.grayscale(image)
    print(f"   Grayscale: average pixel = {sum(sum(p) for p in gray.pixels[0])//30}")
    
    edges = ImageProcessor.edge_detect(image)
    print(f"   Edge detection: processed")
    
    # 7. Data Engineering - ETL
    print("\n7. DATA ENGINEERING - ETL PIPELINE")
    print("-" * 40)
    
    async def extract(data):
        print("     [Extract] Loading raw data...")
        return data
    
    async def transform(data):
        print("     [Transform] Cleaning and normalizing...")
        return [d.upper() for d in data]
    
    async def load(data):
        print("     [Load] Saving to database...")
        return f"Loaded {len(data)} records"
    
    pipeline = ETLPipeline()
    pipeline.add_extractor(extract)
    pipeline.add_transformer(transform)
    pipeline.add_loader(load)
    
    result = await pipeline.run(["task1", "task2", "task3"])
    print(f"   Result: {result}")
    
    # 8. Data Validation
    print("\n8. DATA VALIDATION")
    print("-" * 40)
    
    validator = DataValidator()
    print(f"   Email 'papi@scaleplus.io': {validator.validate_email('papi@scaleplus.io')}")
    print(f"   Email 'invalid': {validator.validate_email('invalid')}")
    print(f"   Phone '+63 912 345 6789': {validator.validate_phone('+63 912 345 6789')}")
    json_test = '{"name": "test"}'
    print(f"   JSON valid: {validator.validate_json(json_test)}")
    
    # 9. Advanced RAG
    print("\n9. ADVANCED RAG - CHUNKING")
    print("-" * 40)
    
    long_text = """ScalePlus.io is a business automation company. 
    We help SMEs grow through AI-powered systems. 
    Our services include Website Lite and Growth System retainers.
    Hayahaya Adventures offers vehicle and equipment rentals.
    Perfect for camping and outdoor activities."""
    
    chunks = Chunker.semantic(long_text, sentences_per_chunk=2)
    print(f"   Original length: {len(long_text)} chars")
    print(f"   Chunks created: {len(chunks)}")
    for i, chunk in enumerate(chunks[:3]):
        print(f"     Chunk {i+1}: {chunk[:50]}...")
    
    # 10. Query Expansion
    print("\n10. ADVANCED RAG - QUERY EXPANSION")
    print("-" * 40)
    
    expander = QueryExpander()
    query = "website price"
    expanded = expander.expand(query)
    
    print(f"   Original: '{query}'")
    print("   Expanded queries:")
    for q in expanded:
        print(f"     - {q}")
    
    print("\n" + "=" * 70)
    print("PHASE 5 CONCEPTS DEMONSTRATED:")
    print("=" * 70)
    concepts = [
        "Tokenization (word, sentence, n-gram)",
        "Text Preprocessing (stopwords, stemming)",
        "TF-IDF Vectorization",
        "Named Entity Recognition (NER)",
        "Sentiment Analysis",
        "Image Processing (grayscale, blur, edges)",
        "OCR Concepts",
        "ETL Pipeline Architecture",
        "Data Validation",
        "Text Chunking (fixed, semantic)",
        "Query Expansion",
        "Re-ranking"
    ]
    for i, concept in enumerate(concepts, 1):
        print(f"  {i:2}. {concept}")
    
    print("\n" + "=" * 70)
    print("ALL 5 PHASES COMPLETE")
    print("=" * 70)
    print("\nPython Mastery Curriculum Finished!")
    print("Ready for production AI/ML development.")


if __name__ == "__main__":
    asyncio.run(main())
