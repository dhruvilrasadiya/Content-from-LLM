# Content Generation App

This is a **Streamlit app** that uses **LLaMA 2 model with LangChain**
to generate content.

------------------------------------------------------------------------

## Setup Instructions

### 1. Clone the Repository

``` bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create Virtual Environment and Activate

``` bash
# Linux / Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Requirements

``` bash
pip install -r requirements.txt
```

### 4. Download Model File

Download **llama-2-7b-chat.ggmlv3.q8_0.bin** from Hugging Face:\
👉 [Download
Model](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML)

### 5. Place Model File

Place the downloaded file inside a folder named **model/** in the
project root:

    project/
     ├─ app.py
     ├─ requirements.txt
     └─ model/
         └─ llama-2-7b-chat.ggmlv3.q8_0.bin

### 6. Run the App

``` bash
streamlit run app.py
```

------------------------------------------------------------------------
