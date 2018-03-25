rm -rf *~ *.dSYM
rm -rf helpers/*~ /helpers/*.dSYM helpers/*.pyc
for i in `seq 1 $1`;
do    
      ./p$i.py
done

