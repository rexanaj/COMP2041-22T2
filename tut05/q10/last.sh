#!/bin/dash

logins=0
z0=0
z1=0
z2=0
z3=0
z4=0
z5=0
z6=0
z7=0
z8=0
z9=0

while read -r zid pts address other ; do 
    # If it's a connection to 'uniwide', then increment my counter for `logins`
    case "$address" in 
        *uniwide*)
            logins=$((logins+1))
            ;;
    esac 

    # Find the distribution of zids 
    case "$zid" in 
        z0*) z0=$((z0+1)) ;;
        z1*) z1=$((z1+1)) ;;
        z2*) z2=$((z2+1)) ;;
        z3*) z3=$((z3+1)) ;;
        z4*) z4=$((z4+1)) ;;
        z5*) z5=$((z5+1)) ;;
        z6*) z6=$((z6+1)) ;;
        z7*) z7=$((z7+1)) ;;
        z8*) z8=$((z8+1)) ;;
        z9*) z9=$((z9+1)) ;;
    esac
done < last.log

echo "Uniwide logins: $logins"
echo "z0 logins: $z0"
echo "z1 logins: $z1"
echo "z2 logins: $z2"
echo "z3 logins: $z3"
echo "z4 logins: $z4"
echo "z5 logins: $z5"
echo "z6 logins: $z6"
echo "z7 logins: $z7"
echo "z8 logins: $z8"
echo "z9 logins: $z9"
 