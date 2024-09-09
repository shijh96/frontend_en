from tn.english.normalizer import Normalizer as EnNormalizer
#import ipdb
en_tn_model = EnNormalizer(cache_dir = "/mnt/d/workspace/WeTextProcessing/tn")

def main():
    with open('test_eng_norm.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    total = 0
    correct = 0
    
    for line in lines:
        line = line.strip()
        if line.startswith('#') or not line:
            continue
        
        parts = line.split('|')
        if len(parts) != 2:
            continue
 
        test_sentence, ground_truth = parts[0].strip(), parts[1].strip()
        
        result = en_tn_model.normalize(test_sentence)
        
        total += 1
        if result == ground_truth:
            correct += 1
        else:
            print(f"不匹配:\n输入: {test_sentence}\n输出: {result}\n预期: {ground_truth}\n")
    
    accuracy = correct / total if total > 0 else 0
    print(f"总计测试: {total}")
    print(f"正确数量: {correct}")
    print(f"准确率: {accuracy:.2%}")

if __name__ == "__main__":
    main()