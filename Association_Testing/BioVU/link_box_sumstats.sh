cd Box_Download/

for anc in AFR EUR
do
  for i in {1..5}
  do
    echo "${anc}-${i}"
    ls *.pheno${i}.${anc}.*
    ln -s *.pheno${i}.${anc}.* BioVU.pheno${i}.${anc}.txt.gz
    ls *.neg_control${i}.${anc}.*
    ln -s *.neg_control${i}.${anc}.* BioVU.neg_control${i}.${anc}.txt.gz
  done
done