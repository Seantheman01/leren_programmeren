tekst = "HVqxBjoZ!?GkqdeOEezAE!?ohNjqRuxojy!?esAX!?dLsZc!? VcpGtt!?gOxjFQkzTDy!?etEyySXt!?dMVfSG!?akOgOdFpje!?aZpjG!?nydTfnQ!q!? nmanp!?aCa!?lIYeTdIl!?l!yYZyVI!?eOm!?mfcBM!?aNteYpX!?aGFlGtW!?lSy!XYh!?,TfgEb!? uD K!?oqpjKodZrz!?mEm r!?ddo!?aFUpe!qwj!?tvZo!? qKBspNfS!?iQXfEoo!?kGSdJlWh!? VTKzOZq!?jdSLdJdKAv!?aVTKun!?rQEvJ!?ictXgAKZY!?gbIdxqGSp!? aEfGvYgv!?bWgDdYZ!?eB !?ngAt!!? D qLljmm!?vhtTdpIqoJZ!?oQyJXBHX!?lupz!?gYAVXXNg!?taWDDVBQDSO!? BQO HIOZLY!?eoTXtn!?eyR!?nYZkIf!?  OrFk!?kJenGc!?lElWj!?e hOwVlpWz!?iVF!?nu odOVXvSP!?ebinLp!? fRwfXGQs!?tWdfhPh!?ruTvo!!?aHBj!PZaHtQ!?kYYk!?tWeNjDqV!?aFMctpAli!?tnIz!?ivq!?eGRNQq!?!KbotZVm"
volgende = False
uitroepteken = False
vraagteken = False
decrypted = ""

for c in tekst:
    
    if volgende:
        decrypted += c
        volgende = False
        
    vraagteken = c == '?'
    volgende = uitroepteken and vraagteken
    uitroepteken = c == '!'      
        

    print(volgende)

print(decrypted)