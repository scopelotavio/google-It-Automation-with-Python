import os

# os.remove()

os.remove('sample_data/novel.txt')
os.rename('sample_data/novel.txt', 'novel2.txt')
print(os.path.exists('sample_data/novel.txt'))