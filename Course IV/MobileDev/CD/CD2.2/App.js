import React, { Component } from 'react';
import { Text, View, Image, StyleSheet, Button, Alert } from 'react-native';

const FixedDimensionsBasics = () => {
  return (
    <View style={{ flex:1 }}>
      <View style={{ flex: 3, backgroundColor: 'white'
      }}> 
      <Text style={styles.title}>5 книжных новинок октября</Text>
      </View>
      <View style={{ flex: 4, backgroundColor: 'lightgray'
      }}>
      <Text style={styles.middle1}>"Кадиш.com" Натан Ингландер.</Text>
      <Text style={styles.middle2}>Издательство "Книжники"</Text>
      </View>
      <View style={{ flex: 8, backgroundColor: 'gray'
      }}>
      <Text style={styles.text}>Ироничная новелла Натана Ингландера, две личные истории культовой Патти Смит, репортаж британской журналистки о будущем человечества, дебютный роман Оушена Вуонга и журналисткое расследование о создании "Моссада". В нашей подборке рассказываем о пяти захватывающих книжных новинках, которые достойны того, чтобы появиться на ваших полках.</Text>
      <Button
      color='purple'
      onPress={() => Alert.alert('Читать далее')}
      title="Читать далее"/>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  text: {
    fontSize: 20,
    textAlign: 'center',
    fontFamily: 'Times New Roman',
    marginTop: 40,
    margin: 10

  },
  title: {
    fontSize: 30,
    fontFamily: 'Times New Roman',
    textAlign: 'center',
    fontWeight: 'bold',
    marginTop: 60
  },
  middle1: {
    fontSize: 25,
    textAlign: 'center',
    fontFamily: 'Times New Roman',
    alignContent: 'center',
    justifyContent: 'center',
    marginTop:60
  },
  middle2: {
    fontSize: 25,
    textAlign: 'center',
    fontFamily: 'Times New Roman',
    alignContent: 'center',
    justifyContent: 'center'
  }
})

export default FixedDimensionsBasics;