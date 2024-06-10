for a in AFR EUR
do
  rm -r $a/Sumstats/ || true
  mkdir -p $a/Sumstats/
  cp ../../Association_Testing/AOU/SAIGE/$a/Saige_Step2_Results/*_nc.txt $a/Sumstats/
  gzip $a/Sumstats/*.txt
  rename -v _nc.txt.gz .saige.gz $a/Sumstats/*
done

# rm anything with <30 cases
# rm ASIAN/Sumstats/cluster_vs_controls_3.saige.gz
