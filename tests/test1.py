import sys
import os

# Simula uma validação de código ou testes
def run_validation():
    print("--- Iniciando a Verificação do Código Python ---")
    
    # Simulação de um erro baseado em uma variável de ambiente, 
    # que o GitHub Actions pode definir para forçar a falha.
    should_fail = os.getenv("SHOULD_FAIL_TEST", "false").lower() == "true"
    
    if should_fail:
        print("❌ VALIDAÇÃO FALHOU: A variável de ambiente 'SHOULD_FAIL_TEST' está definida como True.")
        print("Log: O código contém um erro ou um teste importante falhou.")
        # Retorna 1 (código de erro) para falhar o pipeline do GitHub Actions
        sys.exit(1) 
    else:
        print("✅ VALIDAÇÃO BEM-SUCEDIDA: O código Python passou na verificação.")
        print("Log: Nenhuma falha detectada.")
        # Retorna 0 (código de sucesso)
        sys.exit(0)

if __name__ == "__main__":
    run_validation()