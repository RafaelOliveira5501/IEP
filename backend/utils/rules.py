# backend/utils/rules.py
def apply_rules(features: dict, current_insights: dict) -> dict:
    # current_insights tem listas possivelmente vazias
    forcas = set(current_insights.get("forcas", []))
    desafios = set(current_insights.get("desafios", []))
    metodos = set(current_insights.get("metodos_recomendados", []))

    # Regras exemplo:
    if features.get("atencao") == "baixa":
        metodos.add("atividades curtas")
        desafios.add("atenção limitada")

    if features.get("nivel_leitura") == "iniciante":
        metodos.add("uso de imagens")
        desafios.add("dificuldade em leitura")

    if features.get("interesse_imagem"):
        forcas.add("preferencia por recursos visuais")
        metodos.add("usar imagens")
    if features.get("interesse_numeros"):
        forcas.add("interesse por números")
        metodos.add("atividades com números")
    if features.get("interesse_jogos"):
        metodos.add("jogos educativos")
        forcas.add("engajamento por jogos")

    # ajustar por idade (exemplo)
    if features.get("idade", 0) <= 7:
        metodos.add("atividades lúdicas e curtas")

    return {
        "forcas": sorted(list(forcas)),
        "desafios": sorted(list(desafios)),
        "metodos_recomendados": sorted(list(metodos)),
    }
