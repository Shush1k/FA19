import * as React from 'react';
import { StyleSheet, Text, SafeAreaView, ScrollView, StatusBar,Image,View,ImageBackground,Button,Pressable,Alert } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

function Second({ navigation }) {

    return (
      <View style={styles.container}>
      <Text style={{textAlign:'center', top:180, color:'#4682B4',fontSize:18}}>Вторая страница</Text>
      <View>
      <Pressable style={styles.button_2} onPress={() => navigation.navigate('Первая страница')}>
      <Text style={styles.text}>Назад</Text>
    </Pressable>

     <Pressable style={styles.button_1} onPress={() => navigation.navigate('Третья страница')}>
      <Text style={styles.text}>Третий экран</Text>
    </Pressable>
    </View>
  
    </View>
  );
  }
  const styles = StyleSheet.create({
      container: {
        flex: 1,
        backgroundColor: 'white',
        paddingTop: StatusBar.currentHeight,
        
      },
      button_2: {
        alignItems: 'center',
        justifyContent: 'center',
        paddingVertical: 12,
        paddingHorizontal: 12,
        borderRadius: 40,
        backgroundColor: '#4682B4',
        bottom:-200,
        width:80,
        left: 120,
        height: 45
      },
      button_1: {
        alignItems: 'center',
        justifyContent: 'center',
        paddingVertical: 12,
        paddingHorizontal: 12,
        borderRadius: 40,
        backgroundColor: '#4682B4',
        bottom:-210,
        width:150,
        left: 85,
        height: 45
      },
      text: {
        fontSize: 15,
        lineHeight: 21,
        fontWeight: 'bold',
        color: 'white',
      },
    });
    
  export default Second;