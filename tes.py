from transformers import pipeline

# Inisialisasi pipeline dengan model BART
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Contoh teks
text = "Tenaga surya, sebagai salah satu bentuk energi terbarukan yang paling cepat berkembang, telah menunjukkan potensi yang signifikan dalam mengurangi ketergantungan pada batu bara dan minyak. Pemasangan panel surya di atap rumah dan gedung telah menjadi semakin umum, dan teknologi ini terus berkembang dengan efisiensi yang lebih tinggi dan biaya produksi yang lebih rendah. Selain itu, tenaga angin telah terbukti sebagai sumber energi yang efektif, khususnya di wilayah yang memiliki kecepatan angin yang tinggi.Investasi dalam teknologi energi terbarukan tidak hanya membantu mengurangi emisi gas rumah kaca tetapi juga menciptakan lapangan kerja baru dalam sektor teknologi hijau. Pemerintah di berbagai negara telah mengenalkan berbagai insentif dan kebijakan yang mendukung adopsi energi terbarukan. Misalnya, subsidi dan kredit pajak untuk individu dan perusahaan yang menginstall sistem energi terbarukan.."

# Generate summary
summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
print("Summary:", summary[0]['summary_text'])
