#!/bin/sh
  
  cp $BASE_DIR/../custom-scripts/S41network-config $BASE_DIR/target/etc/init.d
  chmod +x $BASE_DIR/target/etc/init.d/S41network-config

  cp $BASE_DIR/../custom-scripts/S87server-init $BASE_DIR/target/etc/init.d
  chmod +x $BASE_DIR/target/etc/init.d/S87server-init

  cp -r $BASE_DIR/../custom-scripts/embarcados $BASE_DIR/target/opt


