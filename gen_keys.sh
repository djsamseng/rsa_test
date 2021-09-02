#!/bin/bash
echo "A" > message.txt
openssl genrsa -out private.pem 512
openssl rsa -in private.pem -pubout > public.pem

PRKEY_INFO=`openssl rsa -in private.pem -text -noout`

MODULUS=`echo "$PRKEY_INFO" | grep modulus: -A 5 | tail -5`
MODULUS_HEX=`echo $MODULUS | tr -cd [:alnum:]`
echo "\$MODULUS_HEX=$MODULUS_HEX"
echo ""

PREXP=`echo "$PRKEY_INFO" | grep privateExponent: -A 5 | tail -5`
PREXP_HEX=`echo $PREXP | tr -cd [:alnum:]`
echo "\$PREXP_HEX=$PREXP_HEX"
echo ""

PUBEXP_INFO=`echo "$PRKEY_INFO" | grep publicExponent:`
IFS=" "
read -r -a array <<< $PUBEXP_INFO
PUBEXP=`echo "${array[1]}"`
echo "\$PUBEXP=$PUBEXP"

echo ""
