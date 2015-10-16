#!/usr/bin/env python
#coding:utf-8
def strip_word(sentence, words, flag='1'):
	'''
	@func:去除句子sentence中含有word的词，或相反
	@param: sentence需要处理的句子
	@param: words需要剔除的词列表
	@flag: 为true，表示返回去除words的结果,否则返回只含words的结果
	@return: 返回处理的结果
	'''
	results = []
	for word in sentence.split(' '):
		finded = 0

		for w in words:
			if word.find(w) >= 0:
				finded = 1
				if flag=='0':results.append(word)
				break	

		if flag == '1' and  finded == 0: results.append(word)

	return ' '.join(results)

if __name__ == '__main__':
	import sys
	import os

	if len(sys.argv) < 4: 
		print strip_word.__doc__
		sys.exit(-1)		

	flag = sys.argv[1]
	sentence = sys.argv[2]
	if os.path.isfile(sentence):
		try:
			sentence = file(sentence).read()
		except:
			print 'Failed to open file '
		
	words = sys.argv[3:]
	print strip_word(sentence, words, flag)
