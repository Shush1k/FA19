import React from "react"

class App extends React.Component {
  constructor() {
    super()
    this.state = {
      isLoggedIn: false
    }
    this.handleClick = this.handleClick.bind(this)
  }

  handleClick() {
    this.setState(st => {
      return {
        isLoggedIn: !st.isLoggedIn
      }
    })
  }

  render() {
    let buttonText = this.state.isLoggedIn ? "LOG OUT" : "LOG IN"
    let text = this.state.isLoggedIn ? "Logged in" : "Logged out"
    return (
      <div>
        <button onClick={this.handleClick}>{buttonText}</button>
        <h1>{text}</h1>
      </div>
    )
  }
}

export default App