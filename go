for i in `seq 1 $1`;
do    
      ./p$i.py
done
rm -rf *~ *.dSYM
rm -rf helpers/*~ /helpers/*.dSYM helpers/*.pyc
