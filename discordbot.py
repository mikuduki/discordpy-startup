# �C���X�g�[������ discord.py ��ǂݍ���
import discord

# ������Bot�̃A�N�Z�X�g�[�N���ɒu�������Ă�������
TOKEN = 'NzAxNjg3NTQ3OTMxMzk0MTQ5.Xp1JEA.0pYjCMHXw31Ea8snGUDWfw5bQAI'

# �ڑ��ɕK�v�ȃI�u�W�F�N�g�𐶐�
client = discord.Client()




# ���b�Z�[�W��M���ɓ��삷�鏈��
@client.event
async def on_message(message):
    # ���b�Z�[�W���M�҂�Bot�������ꍇ�͖�������
    if message.author.bot:
        return
    # �u/neko�v�Ɣ���������u�ɂ�[��v���Ԃ鏈��
    if message.content == '/neko':
        await message.channel.send('�ɂ�[��')


@client.event
async def on_message(message):
    if message.content == '/touban'

        await message.channel.send(author.role.name)

@client.event
async def on_message(message):

    if message.content == '/omikuji'
        # ����傪Bot�������ꍇ�����������Ȃ��̂�
        if client.user != message.author
            import random
            omikuji = [
                "��g"   if i < 2 else
                "���g"   if 2 <= i < 10 else
                "���g"   if 10 <= i < 20 else
                "�g"     if 20 <= i < 40 else
                "���g"   if 40 <= i < 50 else
                "��"     if 50 <= i < 55 else
                "����"   if 55 <= i < 59 else
                "�勥"   for i in range(61)]

                print(message.author.name+"����̉^����"+omikuji[random.randrange(len(omikuji))]+"�ł��B")

# Bot�̋N����Discord�T�[�o�[�ւ̐ڑ�
client.run(TOKEN)
