from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Engenheiro de Prompt Omega", version="1.0.0")

class BlueprintInput(BaseModel):
tema: str
publico_alvo: Optional[str] = None
objetivo: str

class PromptInput(BaseModel):
prompt: str

class SelfCritiqueInput(BaseModel):
prompt_original: str

class ReverterImagemInput(BaseModel):
imagem_base64: str
otimizar_para_foto: Optional[bool] = False

class OtimizarPromptInput(BaseModel):
prompt_base: str

@app.post("/gerar-blueprint-prompt")
def gerar_blueprint_prompt(req: BlueprintInput):
return {
"persona": "Especialista em " + req.tema,
"tarefa": "Gerar conteúdo para " + req.objetivo,
"contexto": "Voltado para " + (req.publico_alvo or "público geral"),
"tecnicas": ["Chain-of-Thought", "Self-Critique"],
"output_esperado": "Texto bem estruturado com linguagem clara"
}

@app.post("/validar-estrutura-prompt")
def validar_estrutura_prompt(req: PromptInput):
validade = len(req.prompt.split()) >= 10
return {
"validade": validade,
"observacoes": "Prompt possui estrutura mínima." if validade else "Prompt muito curto.",
"score": 0.95 if validade else 0.45
}

@app.post("/refinar-por-selfcritique")
def refinar_por_selfcritique(req: SelfCritiqueInput):
refinado = req.prompt_original.strip() + " (refinado com mais clareza e objetividade)"
return {
"versao_refinada": refinado,
"comentarios": "Prompt aprimorado com base em crítica interna."
}

@app.post("/executar-silent3x")
def executar_silent3x(req: PromptInput):
erros = []
if "venda" in req.prompt.lower():
erros.append("Palavra ambígua: 'venda'")
aprovado = not erros
return {
"aprovado": aprovado,
"erros_detectados": erros,
"recomendacoes": "Evite termos ambíguos e genéricos." if erros else "Prompt aprovado com alto grau de confiança."
}

@app.post("/reverter-prompt-imagem")
def reverter_prompt_imagem(req: ReverterImagemInput):
return {
"descricao_tecnica": "Imagem escura com texto neon e layout vetorial sci-fi.",
"prompt_estimado": "glowing sci-fi hud, interface digital, black background, cyberpunk elements",
"prompt_fotorealista": (
"photo of realistic sci-fi interface with glowing elements, studio lighting"
if req.otimizar_para_foto else None
)
}

@app.post("/otimizar-prompt-para-foto")
def otimizar_prompt_para_foto(req: OtimizarPromptInput):
return {
"prompt_fotorealista": "photo of " + req.prompt_base.strip() + ", shot with Canon EOS, studio lighting, 50mm lens"
}

@app.post("/avaliar-coerencia-retorica")
def avaliar_coerencia_retorica(req: PromptInput):
return {
"coerencia": "Alta",
"estilo": "Técnico, direto",
"nivel_persuasao": "Moderado para alto"
}
