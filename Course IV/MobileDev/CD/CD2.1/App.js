import * as React from 'react';
import { Text, View, StyleSheet, Image, Button, Alert } from 'react-native';
import Constants from 'expo-constants';
import AssetExample from './components/AssetExample';
import { Card } from 'react-native-paper';

export default function App() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Журнал Bright</Text>
      <Card>
        <Text style={styles.back}>Новости</Text>
        <Image style={{justifyContent:"center", alignSelf: "center", width:170, height:100}} source={require("./assets/123.jpeg")}/>
        <Text style={styles.paragraph}>Превращаем стресс в своего помощника</Text>
        <Text style={styles.text}>Исследователи Йельского университета заявляют, что люди, которые рассматривают стресс, как возможность личностного роста , отмечают улучшение качества жизни. Сегодня узнаем, как это работает и как увидеть положительные стороны стресса.</Text>
        <Button
        title="Читать далее"
        color='#949ca3'
        onPress={() => Alert.alert('Лучше избавиться от стресса')}
        />
      </Card>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    backgroundColor: '#c2cdd6',
    padding: 8,
  },
  paragraph: {
    marginTop: 25,
    marginLeft: 24,
    fontSize: 35,
    fontWeight: 'bold',
  },
  back: {
    fontFamily: 'Times New Roman',
    color: 'blue',
    fontSize: 30,
    margin: 15
  },
  title: {
    margin: 20,
    fontSize: 40,
    fontWeight: 'bold',
    alignSelf: "center"
  },
  text: {
    marginLeft: 24,
    marginRight: 24,
    marginTop: 15,
    fontSize: 20,
    marginBottom: 20
  }
});