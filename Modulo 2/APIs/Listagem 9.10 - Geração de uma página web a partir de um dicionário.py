filmes={
    "drama": ["Ainda Estou Aqui","O Poderoso Chefão", "Ela"],
    "comédia": ["Tempos Modernos","American Pie","Dr. Dolittle"],
    "policial": ["O Exterminador do Futuro","O Procurado","Velozes e Furiosos"],
    "guerra": ["Rambo","1917","Até o Último Homem"],
    "terror": ["Hereditário"," Corra!"," O Exorcista","Invocação do Mal","A Entidade"],
     "ação":  ["Farejando Vingança","Kill - O Massacre no Trem","John Wick 4: Baba Yaga","Missão: Impossível - Acerto de Contas Parte Um","O Corvo"],
     "series" ["Dexter","Brooklyn Nine-Nine","Breaking Bad","Stranger Things","La Casa de Papel"],
    "super Herois" ["Flash"," Homem de Ferro","Batman: O Cavaleiro das Trevas","Homem-Aranha no Aranhaverso","Os Vingadores"]
     "suspense" ["Prison Break","Criminal Minds","Sherlock","Orphan Black","O Diabo de Cada Dia"],
}
página=open("filmes.html","w", encoding="utf-8")
página.write("""
<!DOCTYPE html>
    <html lang="pt-BR">
        <head>
        <meta charset="utf-8"> 
        <title>Filmes</title>
             <style>

             </style>
        </head>
        <body> 
""")
for c, v in filmes.items():
    página.write("<h1>%s</h1>" % c)
    for e in v:
        página.write("<h2>%s</h2>" % e)
página.write("""
</body>
</html>
""")
página.close()