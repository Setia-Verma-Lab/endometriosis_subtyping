for a in AFR EUR ASIAN
do
  rm -r $a/Sumstats/ || true
  mkdir $a/Sumstats/
  cp SAIGE/$a/Saige_Step2_Results/*.txt $a/Sumstats/
  gzip $a/Sumstats/*.txt
  rename -v .txt.gz .saige.gz $a/Sumstats/*
done

# rm anything with <30 cases
rm ASIAN/Sumstats/cluster_vs_controls_1.saige.gz
rm ASIAN/Sumstats/cluster_vs_controls_2.saige.gz
rm ASIAN/Sumstats/cluster_vs_controls_3.saige.gz
rm ASIAN/Sumstats/cluster_vs_controls_4.saige.gz
rm ASIAN/Sumstats/cluster_vs_controls_5.saige.gz
