for a in AFR EUR ASIAN
do
  for d in PMBB eMERGE UKBB
  do
    rm ${d}_${a} || true
    ln -s ../Association_Testing_Negative_Control/${d}/${d}_${a} ${d}_${a}
  done
done

for a in AFR EUR ASIAN
do
  for d in AOU
  do
    rm ${d}_${a} || true
    ln -s ../Association_Testing_Negative_Control/${d}/${a} ${d}_${a}
  done
done