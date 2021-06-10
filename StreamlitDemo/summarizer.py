from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch
from summa import keywords,summarizer
from sentence_splitter import SentenceSplitter, split_text_into_sentences
import numpy as np

class Summarizer:
    model_name = 'tuner007/pegasus_paraphrase'
    torch_device =  'cuda' if torch.cuda.is_available() else 'cpu'
    model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)
    tokenizer = PegasusTokenizer.from_pretrained(model_name)
    def textrank(introduction,methodology,results,conclusion,ratio1,ratio2,ratio3,ratio4):

        splitter = SentenceSplitter(language='en')
        sentence_introduction = splitter.split(summarizer.summarize(introduction,ratio=ratio1/100))
        sentence_methodology = splitter.split(summarizer.summarize(methodology,ratio=ratio2/100))
        sentence_results = splitter.split(summarizer.summarize(results,ratio=ratio3/100))
        sentence_conclusion = splitter.split(summarizer.summarize(conclusion,ratio=ratio4/100))
        all_sentences = np.concatenate((np.array(sentence_introduction), np.array(sentence_methodology),np.array(sentence_results),np.array(sentence_conclusion)))
        print(all_sentences)
        return all_sentences

    def Paraphrase(self,sentence_list):
        paraphrase = []

        for i in sentence_list:
            a = self.get_response(self,i,1)
            paraphrase.append(a)
        paraphrase_string=[]
        for j in paraphrase:
            for x in j:
                paraphrase_string.append(x)

        s = ''.join(paraphrase_string)    
        return s
    def joinString(self,paraphrased_list):
        s = ''.join(paraphrased_list)
        return s
    def get_response(self,input_text,num_return_sequences):
        batch = self.tokenizer.prepare_seq2seq_batch([input_text],truncation=True,padding='longest',max_length=60, return_tensors="pt").to(self.torch_device)
        print("done")
        translated = self.model.generate(**batch,min_length=10,max_length=60,num_beams=10, num_return_sequences=num_return_sequences, temperature=1.5)
        print("done1")
        tgt_text = self.tokenizer.batch_decode(translated, skip_special_tokens=True)
        return tgt_text
    def getSummary(self,introduction,ratio1,methodology,ratio2,results,ratio3,conclusion,ratio4):
        sentence=self.textrank(introduction,methodology,results,conclusion,ratio1,ratio2,ratio3,ratio4)
        paraphrase=self.Paraphrase(self,sentence)
        return paraphrase