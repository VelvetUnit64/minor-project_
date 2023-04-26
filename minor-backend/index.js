import cors from 'cors'
import express from 'express'
import mongoose from 'mongoose'

const app = express();

mongoose.set('strictQuery', false);
app.use(express.urlencoded({extended: true}))
app.use(express.json())
app.use(cors())
mongoose.connect(
    'mongodb://localhost:27017/puzzle',
    {useNewUrlParser: true, useUnifiedTopology: true}, (err) => {
      if (err) {
        console.log('Error');
      } else {
        console.log('db connected');
      }
    });



const userSchema = new mongoose.Schema(
    {name: String, email: String, password: String, level: Number})
const User = new mongoose.model('User', userSchema)

app.post('/login', (req, res) => {
    const {email, password} = req.body
    User.findOne({email: email},
        (err, user) => {
  if (user) {
    if (password === user.password) {
      res.send({message: 'Login successful', user: user})
    } else {
      res.send({message: 'Incorrect password'})
    }
  } else {
    res.send({message: 'User not registered'})
  }
})
});



    app.post(
    '/register',
    (req, res) => {
        const {name, email, password} = req.body
        User.findOne({email: email},
        (err, user) => {
  if (user) {
    res.send({message: 'User already registered'})
  } else {
    const user = new User({name, email, password, level: 0})

    user.save(err => {
      if (err) {
        res.send(err);
      } else {
        res.send({message: 'User saved successfully'});
      }
    });
  }
        })

    });

        app.get('/hpage', function(req, res) {
          res.sendFile('C:\e-litmus\e-litmus\lp\hpj.html');
        });

        app.listen(9002, () => {console.log('server is running on port 9002')})
