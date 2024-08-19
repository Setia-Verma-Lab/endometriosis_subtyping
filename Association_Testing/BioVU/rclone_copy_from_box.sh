module load rclone

rm -r Box_Download/ || true

mkdir Box_Download/
rclone copy -P myPennBox:ssverma_shared/Projects/endometriosis_subtyping/endo_subtyping_files_for_biovu/BioVU_Sumstats/ Box_Download/