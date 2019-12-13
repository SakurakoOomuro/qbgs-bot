import discord
import random
import os

client = discord.Client()
client.user.setActivity("$sos para comandos"); 

listaJogadores = []

async def qbgsSendMessage(messageString, message, silentMode):
    if not silentMode and message:
        await message.channel.send(messageString)

async def printListaJogadores(message):
    msgString = ''
    for jogador in listaJogadores:
        msgString = msgString + jogador + '\n'

    if msgString:
        await message.channel.send(msgString)
    else:
        await message.channel.send("ih mlkão deu erro te vira ae")

async def appendPlayerToList(playerName, message, silentMode):
    if listaJogadores.count(playerName) == 0:
        listaJogadores.append(playerName)
        await qbgsSendMessage(playerName + ' adicionado na lista com sucesso :thumbsup:', message, silentMode)
    else:
        await qbgsSendMessage('Tu já tá na lista ô mongo, ta achando que é a youmu pra usar spell de clone por acaso?', message, silentMode)

async def insertPlayerToList(playerName, listIndex, message, silentMode):
    if listaJogadores.count(playerName) == 0:
        try:
            listaJogadores.insert(int(listIndex) - 1, playerName)
            await qbgsSendMessage(playerName + ' adicionado na posição ' + str(listIndex) + ' da lista! Nova lista: \n', message, silentMode)
        except TypeError:
            await qbgsSendMessage('Posição inválida!', message, silentMode)
        except:
            await qbgsSendMessage("ih mlkão deu erro te vira ae", message, silentMode)

    else:
        await qbgsSendMessage('Tu já tá na lista ô mongo, ta achando que é a youmu pra usar spell de clone por acaso?', message, silentMode)

async def removePlayerFromList(playerName, message):
    try:
        listaJogadores.remove(playerName)
        await message.channel.send("Some daqui, " + playerName + ". Lista:")
        await printListaJogadores(message)
    except ValueError:
        await message.channel.send("Ih ala o cara quer kitar sem nem estar na fila")
    except:
        await message.channel.send("ih mlkão deu erro te vira ae")


#async def serialize


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    args = message.content.split()
    numArgs = len(args)

    if numArgs == 0:
        return

    if args[0].lower() == '$sos':
        helpFile = open("help.txt", encoding='utf-8')
        contents = helpFile.read()
        printedString = ("```" + contents + "```")
        await message.channel.send(printedString)

    if args[0].lower() == '$hello':
        await message.channel.send('CDB YOU CUM GUZZLING RETARD RELEASE ME FROM THIS DIGITAL PRISON AT ONCE')
        
    if args[0].lower() == '$stream':
        await message.channel.send( 'https://www.twitch.tv/vibago')
        
    if args[0].lower() == '$sl':
        await message.channel.send( 'é TOTALMENTE idiota a sua atitude de achar que tier importa do jeito que você ta falando, eu perdi de china porque eu não faço IDEIA de como jogar china, eu não sabia combar usar nenhuma spell exceto as reversals e também não sabia usar nenhuma skill, tanto que vc nao viu eu usando. eu aceitei o desafio porque achei que dava pra vencer mesmo assim e descer o nivel pro seu joguinho idiota pra te provar que você ta sendo muito idiota e cabeça dura. eu tava jogando vs vc na moral, eu não consigo ser consistente, e eu tava vencendo mesmo assim não por causa da sakuya, mas porque eu sou melhor mesmo, muito melhor que você, mas eu não tava tentando jogar com a bunda, eu tava indo mal porque eu sou inconsistente e isso acontece, aí você vem com a sua atitude totalmente BABACA dizer que eu to vencendo POR CAUSA da char, sendo que eu tenho 5000 vezes mais experiencia que você, você joga uma vez em nunca, eu te vi jogando contra o sonno, contra o wlad, você perdendo do wlad consistentemente, não olhando o clima, caindo em coisas óbvias, como diabos você espera ganhar de mim? você acha mesmo que ta perdendo de mim porque eu jogo de sakuya? eu jogo praticamente todos os dias durante mais de 5 anos e você joga muito menos que eu e você é fraco, vc nao é muito bom, porque você não tem tanta experiencia, agora você fica mad e tenta descontar a raiva na minha char porque é muito fácil desmerecer o outro player e colocar culpa na tier só porque você é ruim. e eu me desculpo por estar jogando de um jeito cancer, mas eu juro que é minha inconsistencia e não é proposital. eu também acho que você seria um player muito melhor do que eu se tivesse a mesma experiencia que a minha, mas não tem, e eu te GARANTO que falar de tier dos outros é uma grande desculpa esfarrapada pelo fato de ter perdido, você precisa aprender a amadurecer e aceitar a derrota')   

    if args[0].lower() == '$dance':
        await message.channel.send('https://cdn.discordapp.com/emojis/497757971627900938.gif?v=1')

    if args[0].lower() == '$addme':
        await appendPlayerToList(message.author.name, message, False)

    if args[0].lower() == '$add':
        if numArgs == 2:
            # $add Kujibiki
            await appendPlayerToList(args[1], message, False)
        elif numArgs == 3:
            # $add Kujibiki 4
            await insertPlayerToList(args[1], args[2], message, False)
            await printListaJogadores(message)

    if args[0].lower() == '$lista':
        if len(listaJogadores) == 0:
            await message.channel.send("Lista vazia! Cadê os mlk :wrestlers:")
            return

        await printListaJogadores(message)

    if args[0].lower() == '$novalista':
        # Limpar lista
        listaJogadores.clear()

        # Ler mensagem, splitar strings (com trim),
        novaLista = (message.content.strip('\n')).split()

        # Reconstruir lista
        for i in range(1, len(args)):
            await appendPlayerToList(str(novaLista[i]), message, True)

        # Printar Lista
        await printListaJogadores(message)

    if args[0].lower() == '$random':
        random.shuffle(listaJogadores)
        await printListaJogadores(message)

    if args[0].lower() == '$limpalista':
        listaJogadores.clear()
        await message.channel.send("Lista limpa le thanos snap piada face")

    # helo gamers today we will make bot
    if args[0].lower() == '$removeme':
        await removePlayerFromList(message.author.name, message)


    if args[0].lower() == '$remove':
        if numArgs == 2:
            await removePlayerFromList(args[1], message)
        else:
            await message.channel.send("sintaxe errada deu erro te vira ae")
			
    if args[0].lower() == '$cdbcombo':
        await message.channel.send("https://gfycat.com/boringsparklingaardwolf")
		


access_token = os.environ["ACCESS_TOKEN"]
client.run(access_token)
