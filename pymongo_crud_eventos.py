# Arquivo para os estudantes preencherem as lacunas
# Preencha os espaços em branco (______) com o código correto para interagir com o MongoDB

# LACUNA 1: Importe a função get_database do arquivo pymongo_get_connection_eventos

from pymongo_get_connection_eventos import get_database 

def main():
    # 1. Obtendo a conexão com o banco de dados
    dbname = get_database()
    if dbname is None:
        print("Não foi possível conectar ao banco de dados. Encerrando.")
        return

    # 2. Selecionando a coleção 'participantes'
    # LACUNA 2: Nome da coleção
    colecao = dbname['participantes']

    print("\n--- 1. INSERÇÃO (Create) ---")
    # LACUNA 3: Crie a estrutura do documento a ser inserido, inclua pelo menos 4 campos
    NovoParticipante = {"_id": "part0022","nome":"Ana-joana","email":"anajoana@gmail.com","idade":35}
    # Inserindo um único documento
    # Dica: Qual método usamos para inserir apenas UM documento?
    colecao.insert_one(NovoParticipante) # LACUNA 4: Método de inserção
    print("Participante inserido com sucesso!")

    print("\n--- 2. CONSULTA (Read) ---")
    # Buscando o participante recém-inserido pelo ID
    # LACUNA 5: Crie um filtro de busca para a coleção que você selecionou
    filtro_busca = {"_id": "part0022"}
    
    # Dica: Qual método usamos para buscar apenas UM documento?
    # LACUNA 5: Método de busca
    participante_encontrado = colecao.find(filtro_busca)
    print(f"Participante encontrado: {participante_encontrado}")

    print("\n--- 3. ATUALIZAÇÃO (Update) ---")
    # LACUNA 6: Crie um filtro para atualização
    filtro_update = {"_id": "part018"}
    # LACUNA 7: Monte a estrutura de atualização
    novos_valores ={"$set":{"confirmado": False}}
    # LACUNA 8: Teste a atualização
    colecao.update_one(filtro_update,novos_valores)
    print("Participante atualizado com sucesso!")

    print("\n--- 4. EXCLUSÃO (Delete) ---")
    # Excluindo o participante de teste
    # LACUNA 9: Crie um filtro para exclusão
    filtro_delete = {"_id": "part0021"}
    #Sobre o "_id" : "part0021",havia criado este inicialmente, mas na primeira vez que rodei deu erro, antes desta linha, então ela não rodou.
    # Para lidar com isso usei o primeiro elemento como o filtro do delete.
    
    # Dica: Qual método usamos para excluir apenas UM documento?
    colecao.delete_one(filtro_delete) # LACUNA 6: Método de exclusão
    print("Participante excluído com sucesso!")
    
    print("\n--- 5. CONSULTA AVANÇADA ---")
    # Crie uma consulta utilizando agregação ou operadores de comparação
    pepilene = [
      
        {
            "$group": {"_id": "$idade"},"maiorQue":{"$gt": 30}#a ideia era pegar os participantes que tinha idade maior que 30
        },
        {"$sort": {"maiorQue":{"$sum": -1}}}#aqui seria a forma de lista-lós em ordem decrecente.
    ]
    ConsultaAvancada = colecao.aggregate(pepilene)
    for doc in ConsultaAvancada:
        print(doc)#já aqui seria mostra os elementos um a um, em sua respectiva ordem(decrecente)
    # Faça um comentário, indocando o que a consulta faz, exemplo: Listando os participantes em ordem alfabética
    

if __name__ == "__main__":
    main()
