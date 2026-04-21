import os
import time
from pymongo import MongoClient

def registrar_dados_esg():
    # A URI é configurada pelo Docker Compose para conectar no container 'db'
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
    
    try:
        client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
        db = client.cidades_esg
        
        # Este é o dado que aparecerá no seu MongoDB Compass
        registro = {
            "cidade": "Londrina",
            "tipo_residuo": "Plástico Reciclável",
            "quantidade_kg": 150.5,
            "data_coleta": time.strftime("%Y-%m-%d %H:%M:%S"),
            "status": "Processado via Pipeline CI/CD"
        }
        
        resultado = db.coletas.insert_one(registro)
        
        print("-" * 30)
        print("✅ CONEXÃO COM MONGODB: SUCESSO")
        print(f"✅ REGISTRO INSERIDO: {resultado.inserted_id}")
        print("-" * 30)
        
    except Exception as e:
        print(f"❌ ERRO: {e}")

if __name__ == "__main__":
    registrar_dados_esg()