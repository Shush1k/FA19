import React from 'react';
import { StatusBar } from "react"
import { StyleSheet, Text, View, Image,Button,Alert} from 'react-native';

export default function App() {
  function press(){
    Alert.alert("Ультрамегахарош !", "pepeJAMpepeJAMpepeJAMpepeJAMpepeJAMpepeJAM")
  }
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Some information!</Text>
      <Image style={styles.logo}resizeMode='contain' source={require('./assets/3x.gif')}/>
      <Button color='#31B8AC' title="Запись" onPress={press}/>
  </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex:1,
    backgroundColor: 'white',
    alignItems: 'center',
    justifyContent: 'center',
  },
  logo:{
    width: 300,
    height: 300,
  },
  text:{
    color:'#31B8AC',
    fontWeight: "bold",
    fontSize: 17,
      },

});