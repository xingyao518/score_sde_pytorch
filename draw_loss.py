from matplotlib.pylab import plt


train_loss = []
val_loss = []
with open('workdir/stdout.txt') as f:
    for line in f:
        if 'training_loss:' in line:
            train_loss.append(float(line.split()[-1]))
        elif 'eval_loss:' in line:
            val_loss.append(float(line.split()[-1]))

        if len(val_loss) > 200:
            break

iterations = list(range(0, 50*len(train_loss), 50))

plt.plot(iterations, train_loss, label='Training Loss')
plt.plot(iterations, val_loss, label='Validation Loss')

plt.title('Training and Validation Loss')
plt.xlabel('Iterations')
plt.ylabel('Loss')
plt.xticks(list(range(0, 50*len(train_loss), 1000)))

plt.legend(loc='best')
plt.tight_layout()
plt.savefig('loss.png')

