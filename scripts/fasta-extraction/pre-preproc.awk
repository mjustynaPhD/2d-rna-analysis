$0 == "_atom_site.auth_seq_id" { print("_atom_site.pdbx_formal_charge\n_atom_site.auth_seq_id"); }
$0 ~ /^ATOM/ || $0 ~ /^HETATM/ {
	b = 2;
	firstSpace = 0;
	for(i=1;i<=length($0);i++) {
		if (substr($0,i,1) == " " && !firstSpace)
			firstSpace = 1;
		else if (substr($0,i,1) != " " && firstSpace) {
			a[b++] = i;
			firstSpace = 0;
		}
	}
	idx = a[NF-4];
	printf("%s? %s\n", substr($0,1,idx-1), substr($0,idx));
}
$0 !~ /^ATOM/ && $0 !~ /^HETATM/ && $0 != "_atom_site.auth_seq_id" {print $0;}