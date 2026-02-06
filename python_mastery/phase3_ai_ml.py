#!/usr/bin/env python3
"""
Phase 3: AI / Machine Learning
PyTorch, LLM Integration, RAG Systems
"""

import asyncio
import json
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Any, Optional, Protocol, Callable, Tuple
from enum import Enum
import urllib.request
import urllib.error
from collections import defaultdict
import math


# ============== Neural Network Fundamentals ==============

class Tensor:
    """Minimal tensor implementation for educational purposes.
    Demonstrates how PyTorch/NumPy operations work at fundamental level.
    """
    
    def __init__(self, data: List[List[float]]):
        self.data = data
        self.shape = (len(data), len(data[0]) if data else 0)
    
    def __add__(self, other: 'Tensor') -> 'Tensor':
        """Element-wise addition."""
        if self.shape != other.shape:
            raise ValueError("Shape mismatch")
        return Tensor([
            [a + b for a, b in zip(row_a, row_b)]
            for row_a, row_b in zip(self.data, other.data)
        ])
    
    def __mul__(self, scalar: float) -> 'Tensor':
        """Scalar multiplication."""
        return Tensor([[x * scalar for x in row] for row in self.data])
    
    def dot(self, other: 'Tensor') -> 'Tensor':
        """Matrix multiplication."""
        if self.shape[1] != other.shape[0]:
            raise ValueError("Shape incompatible for dot product")
        
        result = []
        for i in range(self.shape[0]):
            row = []
            for j in range(other.shape[1]):
                # Dot product of row i from self and column j from other
                value = sum(
                    self.data[i][k] * other.data[k][j]
                    for k in range(self.shape[1])
                )
                row.append(value)
            result.append(row)
        return Tensor(result)
    
    def relu(self) -> 'Tensor':
        """ReLU activation: max(0, x)"""
        return Tensor([[max(0, x) for x in row] for row in self.data])
    
    def softmax(self) -> 'Tensor':
        """Softmax activation for probability distribution."""
        result = []
        for row in self.data:
            exp_sum = sum(math.exp(x) for x in row)
            result.append([math.exp(x) / exp_sum for x in row])
        return Tensor(result)
    
    def __repr__(self):
        return f"Tensor(shape={self.shape}, data={self.data})"


class Layer(ABC):
    """Abstract base for neural network layers."""
    
    @abstractmethod
    def forward(self, x: Tensor) -> Tensor: ...
    
    @abstractmethod
    def backward(self, grad: Tensor) -> Tensor: ...


class Linear(Layer):
    """Fully connected linear layer: y = Wx + b"""
    
    def __init__(self, in_features: int, out_features: int):
        # Xavier initialization
        scale = math.sqrt(2.0 / (in_features + out_features))
        self.weights = Tensor([
            [scale * (2 * (i + j) % 2 - 1) for j in range(out_features)]
            for i in range(in_features)
        ])
        self.bias = Tensor([[0.0] * out_features])
        self._input: Optional[Tensor] = None
    
    def forward(self, x: Tensor) -> Tensor:
        self._input = x
        # x @ weights + bias
        output = x.dot(self.weights)
        # Add bias to each row
        biased = [[val + self.bias.data[0][j] for j, val in enumerate(row)] 
                  for row in output.data]
        return Tensor(biased)
    
    def backward(self, grad: Tensor) -> Tensor:
        # Simplified gradient computation
        return grad.dot(Tensor([[1.0]]))  # Placeholder


class ReLU(Layer):
    """ReLU activation layer."""
    
    def forward(self, x: Tensor) -> Tensor:
        return x.relu()
    
    def backward(self, grad: Tensor) -> Tensor:
        # Gradient is 1 where input > 0, else 0
        return grad


class NeuralNetwork:
    """Simple feedforward neural network."""
    
    def __init__(self):
        self.layers: List[Layer] = []
    
    def add(self, layer: Layer):
        self.layers.append(layer)
    
    def forward(self, x: Tensor) -> Tensor:
        for layer in self.layers:
            x = layer.forward(x)
        return x
    
    def predict(self, x: List[List[float]]) -> Tensor:
        return self.forward(Tensor(x))


# ============== LLM Integration ==============

class LLMProvider(ABC):
    """Abstract interface for LLM providers."""
    
    @abstractmethod
    async def complete(self, prompt: str, **kwargs) -> str: ...
    
    @abstractmethod
    async def chat(self, messages: List[Dict[str, str]], **kwargs) -> str: ...


class OpenAIClient(LLMProvider):
    """OpenAI API client implementation."""
    
    def __init__(self, api_key: str, model: str = "gpt-4"):
        self.api_key = api_key
        self.model = model
        self.base_url = "https://api.openai.com/v1"
    
    async def complete(self, prompt: str, temperature: float = 0.7) -> str:
        """Text completion endpoint."""
        return await self._request("completions", {
            "model": self.model,
            "prompt": prompt,
            "temperature": temperature,
            "max_tokens": 500
        })
    
    async def chat(self, messages: List[Dict[str, str]], temperature: float = 0.7) -> str:
        """Chat completion endpoint."""
        return await self._request("chat/completions", {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": 500
        })
    
    async def _request(self, endpoint: str, data: Dict) -> str:
        """Make authenticated API request."""
        def make_request():
            req = urllib.request.Request(
                f"{self.base_url}/{endpoint}",
                method="POST",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                data=json.dumps(data).encode('utf-8')
            )
            try:
                with urllib.request.urlopen(req, timeout=30) as response:
                    result = json.loads(response.read().decode('utf-8'))
                    # Extract text from response
                    if 'choices' in result:
                        choice = result['choices'][0]
                        return choice.get('message', {}).get('content', '') or \
                               choice.get('text', '')
                    return ''
            except urllib.error.HTTPError as e:
                return f"API Error: {e.code}"
        
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, make_request)


# ============== Prompt Engineering ==============

class PromptTemplate:
    """Template for structured prompting."""
    
    def __init__(self, template: str, variables: List[str]):
        self.template = template
        self.variables = variables
    
    def format(self, **kwargs) -> str:
        """Fill in template variables."""
        result = self.template
        for var in self.variables:
            if var in kwargs:
                result = result.replace(f"{{{var}}}", str(kwargs[var]))
        return result


class PromptLibrary:
    """Library of optimized prompts."""
    
    TASK_EXTRACTION = PromptTemplate(
        """Extract tasks from the following message and format as JSON.
        
Message: {message}

Extract:
1. Task name (clear, actionable)
2. Priority (high/medium/low)
3. Due date if mentioned
4. Assignee if mentioned

Output JSON format:
{{
    "tasks": [
        {{
            "name": "task description",
            "priority": "high/medium/low",
            "due_date": "YYYY-MM-DD or null",
            "assignee": "name or null"
        }}
    ]
}}""",
        ["message"]
    )
    
    BUSINESS_ANALYSIS = PromptTemplate(
        """Analyze this business request for ScalePlus.io:

Client Message: {message}

Determine:
1. Service type (Website Lite / Growth System)
2. Estimated scope (small/medium/large)
3. Qualification questions to ask
4. Next steps

Format as structured analysis.""",
        ["message"]
    )
    
    CODE_REVIEW = PromptTemplate(
        """Review this Python code for best practices:

```python
{code}
```

Check for:
1. PEP 8 compliance
2. Type hints
3. Error handling
4. Performance issues
5. Security concerns

Provide specific recommendations.""",
        ["code"]
    )


# ============== RAG (Retrieval Augmented Generation) ==============

@dataclass
class Document:
    """Document for RAG system."""
    id: str
    content: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    embedding: Optional[List[float]] = None


class EmbeddingModel(ABC):
    """Interface for text embedding models."""
    
    @abstractmethod
    def embed(self, text: str) -> List[float]: ...


class SimpleEmbeddingModel(EmbeddingModel):
    """Simple bag-of-words embedding for demonstration."""
    
    def __init__(self, vocab_size: int = 1000):
        self.vocab_size = vocab_size
        self.word_to_idx: Dict[str, int] = {}
        self.idx = 0
    
    def _tokenize(self, text: str) -> List[str]:
        """Simple tokenization."""
        return re.findall(r'\b\w+\b', text.lower())
    
    def embed(self, text: str) -> List[float]:
        """Create embedding vector."""
        tokens = self._tokenize(text)
        vector = [0.0] * self.vocab_size
        
        for token in tokens:
            if token not in self.word_to_idx:
                self.word_to_idx[token] = self.idx
                self.idx = (self.idx + 1) % self.vocab_size
            
            idx = self.word_to_idx[token]
            vector[idx] += 1.0
        
        # Normalize
        magnitude = math.sqrt(sum(x**2 for x in vector))
        if magnitude > 0:
            vector = [x / magnitude for x in vector]
        
        return vector


class VectorStore:
    """In-memory vector database for RAG."""
    
    def __init__(self, embedding_model: EmbeddingModel):
        self.model = embedding_model
        self.documents: Dict[str, Document] = {}
        self.vectors: Dict[str, List[float]] = {}
    
    def add(self, doc: Document):
        """Add document to store."""
        doc.embedding = self.model.embed(doc.content)
        self.documents[doc.id] = doc
        self.vectors[doc.id] = doc.embedding
    
    def search(self, query: str, top_k: int = 3) -> List[Tuple[Document, float]]:
        """Search for similar documents using cosine similarity."""
        query_vector = self.model.embed(query)
        
        scores = []
        for doc_id, vector in self.vectors.items():
            similarity = self._cosine_similarity(query_vector, vector)
            scores.append((self.documents[doc_id], similarity))
        
        # Sort by similarity descending
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_k]
    
    def _cosine_similarity(self, a: List[float], b: List[float]) -> float:
        """Calculate cosine similarity between two vectors."""
        dot = sum(x * y for x, y in zip(a, b))
        mag_a = math.sqrt(sum(x**2 for x in a))
        mag_b = math.sqrt(sum(x**2 for x in b))
        return dot / (mag_a * mag_b) if mag_a * mag_b > 0 else 0.0


class RAGSystem:
    """Retrieval Augmented Generation system."""
    
    def __init__(self, llm: LLMProvider, vector_store: VectorStore):
        self.llm = llm
        self.store = vector_store
    
    async def query(self, question: str, system_prompt: str = "") -> str:
        """Query with context retrieval."""
        # 1. Retrieve relevant documents
        relevant_docs = self.store.search(question, top_k=3)
        
        # 2. Build context
        context = "\n\n".join([
            f"Document {i+1}:\n{doc.content}"
            for i, (doc, score) in enumerate(relevant_docs)
        ])
        
        # 3. Build augmented prompt
        prompt = f"""{system_prompt}

Context information:
{context}

Based on the context above, answer this question:
{question}

Answer:"""
        
        # 4. Generate response
        return await self.llm.complete(prompt, temperature=0.3)
    
    async def add_knowledge(self, content: str, metadata: Dict = None):
        """Add knowledge to the system."""
        doc = Document(
            id=f"doc_{len(self.store.documents)}",
            content=content,
            metadata=metadata or {}
        )
        self.store.add(doc)


# ============== Chains (LangChain-style) ==============

class Chain(ABC):
    """Abstract chain for sequential operations."""
    
    @abstractmethod
    async def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]: ...


class SequentialChain(Chain):
    """Chain that runs steps sequentially."""
    
    def __init__(self, steps: List[Chain]):
        self.steps = steps
    
    async def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        result = inputs
        for step in self.steps:
            result = await step.run(result)
        return result


class LLMChain(Chain):
    """Chain step that calls an LLM."""
    
    def __init__(self, llm: LLMProvider, prompt_template: PromptTemplate, 
                 output_key: str = "response"):
        self.llm = llm
        self.template = prompt_template
        self.output_key = output_key
    
    async def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        prompt = self.template.format(**inputs)
        response = await self.llm.complete(prompt)
        return {**inputs, self.output_key: response}


class TransformChain(Chain):
    """Chain step that transforms data."""
    
    def __init__(self, transform_fn: Callable, input_key: str, output_key: str):
        self.transform = transform_fn
        self.input_key = input_key
        self.output_key = output_key
    
    async def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        value = inputs.get(self.input_key)
        transformed = self.transform(value)
        return {**inputs, self.output_key: transformed}


# ============== Agents ==============

class Tool(ABC):
    """Tool for agent to use."""
    
    name: str
    description: str
    
    @abstractmethod
    async def run(self, input_str: str) -> str: ...


class NotionTool(Tool):
    """Tool for Notion operations."""
    
    name = "notion"
    description = "Create and query tasks in Notion"
    
    async def run(self, input_str: str) -> str:
        # Would integrate with Notion API
        return f"Created Notion task: {input_str}"


class SearchTool(Tool):
    """Tool for web search."""
    
    name = "search"
    description = "Search the web for information"
    
    async def run(self, input_str: str) -> str:
        # Would integrate with search API
        return f"Search results for: {input_str}"


class Agent:
    """LLM-powered agent with tool use."""
    
    def __init__(self, llm: LLMProvider, tools: List[Tool]):
        self.llm = llm
        self.tools = {tool.name: tool for tool in tools}
    
    async def run(self, task: str) -> str:
        """Execute task using available tools."""
        # Build system prompt with tool descriptions
        tool_descriptions = "\n".join([
            f"- {name}: {tool.description}"
            for name, tool in self.tools.items()
        ])
        
        prompt = f"""You are an AI assistant with access to tools.

Available tools:
{tool_descriptions}

Task: {task}

Think step by step. If you need to use a tool, respond with:
TOOL: tool_name
INPUT: tool_input

If you can answer directly, respond with:
ANSWER: your_response"""
        
        response = await self.llm.complete(prompt, temperature=0.3)
        
        # Parse response
        if "TOOL:" in response:
            lines = response.strip().split('\n')
            tool_name = lines[0].replace("TOOL:", "").strip()
            tool_input = lines[1].replace("INPUT:", "").strip() if len(lines) > 1 else ""
            
            if tool_name in self.tools:
                tool_result = await self.tools[tool_name].run(tool_input)
                # Follow-up with result
                followup = await self.llm.complete(
                    f"Tool result: {tool_result}\n\nProvide final answer.",
                    temperature=0.3
                )
                return followup
        
        return response.replace("ANSWER:", "").strip()


# ============== Main ==============

async def main():
    """Demonstrate Phase 3 AI/ML concepts."""
    print("=" * 70)
    print("PHASE 3: AI / MACHINE LEARNING")
    print("=" * 70)
    
    # 1. Neural Network from Scratch
    print("\n1. NEURAL NETWORK FUNDAMENTALS")
    print("-" * 40)
    
    # Create simple network: input (3) -> hidden (4) -> output (2)
    nn = NeuralNetwork()
    nn.add(Linear(3, 4))  # Input to hidden
    nn.add(ReLU())         # Activation
    nn.add(Linear(4, 2))  # Hidden to output
    
    # Sample input: [hours_worked, complexity_score, urgency_score]
    sample_input = [[8.0, 0.7, 0.9]]  # High complexity, urgent
    prediction = nn.predict(sample_input)
    print(f"   Input: {sample_input}")
    print(f"   Output: {prediction.data}")
    print(f"   → Raw prediction scores (would apply softmax for probabilities)")
    
    # 2. Tensor Operations
    print("\n2. TENSOR OPERATIONS (like PyTorch)")
    print("-" * 40)
    
    a = Tensor([[1.0, 2.0], [3.0, 4.0]])
    b = Tensor([[5.0, 6.0], [7.0, 8.0]])
    
    print(f"   Matrix A: {a.data}")
    print(f"   Matrix B: {b.data}")
    print(f"   A + B: {(a + b).data}")
    print(f"   A * 2: {(a * 2).data}")
    print(f"   A · B (dot): {(a.dot(b)).data}")
    
    # 3. Embeddings
    print("\n3. TEXT EMBEDDINGS")
    print("-" * 40)
    
    embedder = SimpleEmbeddingModel(vocab_size=50)
    
    texts = [
        "Create website for client",
        "Build landing page",
        "Design growth system",
        "Setup automation workflow"
    ]
    
    embeddings = [embedder.embed(text) for text in texts]
    print(f"   Embedded {len(texts)} documents")
    print(f"   Vector dimension: {len(embeddings[0])}")
    
    # Show similarity
    def cosine_sim(a, b):
        dot = sum(x * y for x, y in zip(a, b))
        mag_a = math.sqrt(sum(x**2 for x in a))
        mag_b = math.sqrt(sum(x**2 for x in b))
        return dot / (mag_a * mag_b) if mag_a * mag_b > 0 else 0.0
    
    query = embedder.embed("website development")
    similarities = [
        (text, cosine_sim(query, emb))
        for text, emb in zip(texts, embeddings)
    ]
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    print("\n   Query: 'website development'")
    print("   Top matches:")
    for text, score in similarities[:3]:
        print(f"     {score:.3f} - {text}")
    
    # 4. RAG System
    print("\n4. RAG (RETRIEVAL AUGMENTED GENERATION)")
    print("-" * 40)
    
    # Mock LLM for demo
    class MockLLM(LLMProvider):
        async def complete(self, prompt: str, **kwargs) -> str:
            return f"[LLM would answer based on context]"
        async def chat(self, messages: List[Dict], **kwargs) -> str:
            return "Mock response"
    
    rag = RAGSystem(MockLLM(), VectorStore(SimpleEmbeddingModel()))
    
    # Add knowledge
    await rag.add_knowledge(
        "ScalePlus.io offers Website Lite (3 pages) at 4,995 PHP/month",
        {"service": "Website Lite"}
    )
    await rag.add_knowledge(
        "ScalePlus.io offers Growth System retainer at 9,995 PHP/month",
        {"service": "Growth System"}
    )
    await rag.add_knowledge(
        "Hayahaya Adventures rents Jimny for 3,500 PHP/day with Starlink",
        {"service": "Vehicle Rental"}
    )
    
    results = rag.store.search("website pricing", top_k=2)
    print("   Added 3 documents to knowledge base")
    print("   Search: 'website pricing'")
    for doc, score in results:
        print(f"     {score:.3f} - {doc.content[:50]}...")
    
    # 5. Prompt Engineering
    print("\n5. PROMPT ENGINEERING")
    print("-" * 40)
    
    message = "Papi needs to finish the DTI registration for Hayahaya by tomorrow"
    prompt = PromptLibrary.TASK_EXTRACTION.format(message=message)
    
    print("   Template: TASK_EXTRACTION")
    print(f"   Input: '{message[:50]}...'")
    print("   Generated prompt (truncated):")
    print(f"     {prompt[:200]}...")
    
    # 6. Chains
    print("\n6. LANGCHAIN-STYLE CHAINS")
    print("-" * 40)
    
    chain = SequentialChain([
        TransformChain(lambda x: x.upper(), "input", "uppercase"),
        TransformChain(lambda x: len(x), "uppercase", "length")
    ])
    
    result = await chain.run({"input": "Hello World"})
    print(f"   Chain: input → uppercase → length")
    print(f"   Result: {result}")
    
    # 7. Agents
    print("\n7. AI AGENTS WITH TOOLS")
    print("-" * 40)
    
    agent = Agent(MockLLM(), [NotionTool(), SearchTool()])
    print("   Agent with tools:")
    print("     - notion: Create Notion tasks")
    print("     - search: Web search")
    print("   Agent can reason about when to use each tool")
    
    print("\n" + "=" * 70)
    print("PHASE 3 CONCEPTS DEMONSTRATED:")
    print("=" * 70)
    concepts = [
        "Neural Networks (from scratch)",
        "Tensor Operations (matrix math)",
        "Forward propagation",
        "Activation functions (ReLU)",
        "LLM Provider Interface (OpenAI)",
        "Prompt Templates",
        "Text Embeddings",
        "Vector Similarity Search",
        "RAG Architecture",
        "Retrieval + Generation",
        "Sequential Chains",
        "Tool-using Agents"
    ]
    for i, concept in enumerate(concepts, 1):
        print(f"  {i:2}. {concept}")
    
    print("\n" + "=" * 70)
    print("PHASE 3 COMPLETE")
    print("=" * 70)
    print("\nNext: Phase 4 - Production Systems (FastAPI, Docker, Deployment)")


if __name__ == "__main__":
    asyncio.run(main())
