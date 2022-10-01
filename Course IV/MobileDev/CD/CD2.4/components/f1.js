import * as React from 'react';
import { StyleSheet, Text, StatusBar,Image,View,Pressable,Alert } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';


function First({ navigation }) {

  return (
    <View style={styles.container}>
    <Text style={{textAlign:'center', top:180, color:'#4682B4',fontSize:18}}>
        Первый экран</Text>
        
    <Pressable style={styles.button_1} onPress={() => navigation.navigate('Вторая страница')}>
      <Text style={styles.text}>Перейти на второй экран</Text>
    </Pressable>

  </View>
);
}
const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: 'white',
      paddingTop: StatusBar.currentHeight,
      
    },
    button_1: {
      alignItems: 'center',
      justifyContent: 'center',
      paddingVertical: 12,
      borderRadius: 40,
      backgroundColor: '#4682B4',
      top:100,
      width:270,     
      left: 70, 
    },
    text: {
      fontSize: 15,
      lineHeight: 21,
      fontWeight: 'bold',
      color: 'white',
    },
  });
  
export default First;