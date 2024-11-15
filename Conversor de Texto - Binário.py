import tkinter as tk
from tkinter import ttk

def converter_para_binario():
    texto = entrada_texto.get("1.0", tk.END).strip()
    if texto:
        binario = ' '.join(format(ord(char), '08b') for char in texto)
        resultado_texto.delete("1.0", tk.END)
        resultado_texto.insert(tk.END, binario)
    else:
        resultado_texto.delete("1.0", tk.END)
        resultado_texto.insert(tk.END, "Por favor, insira algum texto.")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Conversor de Texto para Binário")
janela.geometry("600x400")
janela.configure(bg="#f0f8ff")  # Cor de fundo

# Label para entrada
label_entrada = tk.Label(janela, text="Digite o texto:", font=("Arial", 14), bg="#f0f8ff", fg="#000080")
label_entrada.pack(pady=10)

# Caixa de texto para entrada
entrada_texto = tk.Text(janela, height=5, width=60, font=("Arial", 12), bg="#e6f7ff", fg="#000000")
entrada_texto.pack(pady=5)

# Botão para converter
botao_converter = tk.Button(janela, text="Converter para Binário", command=converter_para_binario, font=("Arial", 12, "bold"), bg="#800080", fg="#FAFAD2")
botao_converter.pack(pady=10)

# Label para resultado
label_resultado = tk.Label(janela, text="Texto em binário:", font=("Arial", 14), bg="#f0f8ff", fg="#000080")
label_resultado.pack(pady=10)

# Caixa de texto para resultado
resultado_texto = tk.Text(janela, height=5, width=60, font=("Arial", 12), bg="#fff5e6", fg="#000000")
resultado_texto.pack(pady=5)

# Iniciar a aplicação
janela.mainloop()
