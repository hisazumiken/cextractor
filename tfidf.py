import json
import math
import sys

# dfitf [total.dict] [num] [.c.dict]

if __name__ == "__main__":
    alldict = {}
    with open(sys.argv[1]) as file:
        alldict = json.load(file)
    docnum = int(sys.argv[2])

    cdict = {}
    with open(sys.argv[3]) as file:
        cdict = json.load(file)
    
    term_num = sum(int(i) for i in cdict.values())
    metrics = {}
    for k, num in cdict.items():
        idf = math.log(docnum/float(alldict[k]))
        tf = float(num)/term_num
        tfidf = tf * idf
        # lower is better
        metrics[k] = (tfidf, tf, idf)

# for debugging metric
#    for k, mx in sorted(metrics.items(), key=lambda x: -x[1][0]):
#        print("%s: %f %f %f" % (k, mx[0], mx[1], mx[2]))

    filtered = {k:v[0] for (k,v) in metrics.items() if v[0] < 1.0}
    print(json.dumps(filtered))

    
