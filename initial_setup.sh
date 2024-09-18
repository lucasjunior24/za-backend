import os
import subprocess
import sys

def create_venv(diretorio_projeto: str):
  if not os.path.exists(diretorio_projeto):
    print(f"O diretorio {diretorio_projeto} não existe!")
    return
  
  venv_path = os.path.join(diretorio_projeto, '.venv')
  print(venv_path)
  if os.path.exists(venv_path):
    print("O ambiente virtual já existe!")
    return
  
  try:
    subprocess.run(['python', '-m', 'venv', '.venv'])
    print("Venv criado com sucesso!")
  
  except subprocess.CalledProcessError as error:
    print(F"Erro ao criar venv: {error}")


def install_dependencias(diretorio_projeto: str, requirement_file: str):
  if not os.path.exists(requirement_file):
    print(f"O arquivo {requirement_file} não existe!")
    return
  
  venv_path = os.path.join(diretorio_projeto, ".venv", "bin", "activate")

  print()
  print(venv_path)

  subprocess.run(['source', venv_path], shell=True)

  # try:
  #   subprocess.run(['pip', 'install', '-r', requirement_file])
  #   print("Dependências instaladas!")
  
  # except subprocess.CalledProcessError as error:
  #   print(F"Erro ao instalar dependências: {error}")
  

def main():
  if len(sys.argv) != 2:
    print("Uso: python name.py /caminho/do/diretorio")
    sys.exit()

  diretorio_projeto = sys.argv[1]
  requirements_file = os.path.join(diretorio_projeto, 'requirements.txt')
  
  print(requirements_file)
  create_venv(diretorio_projeto)
  # subprocess.run(["source", './.venv/Scripts/activate'], shell=True)
  install_dependencias(diretorio_projeto, requirements_file)


if __name__ == '__main__':
  main()