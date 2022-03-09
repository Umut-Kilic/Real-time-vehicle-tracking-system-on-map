$.ajax({
    url: '/30_dakkalik_arabalar',
    type: 'GET',

    success: function (data) {

      for (let i = 0; i < data['cars'].length; i++) {
        // console.log(['cars'][i])
        id = data['cars'][i]['id']
        console.log(id)
        for (let j = 0; j < data['cars'][i]['features'].length; j++) {

          var arac={
            id:data['cars'][i]['id'],
            x:data['cars'][i]['features'][j]['x'],
            y:data['cars'][i]['features'][j]['y']
          }
          araclar.push(arac)
          if(araclar.length>30)
            araclar.shift()
        }
      }
      console.log(araclar)
      module.exports = {araclar}
    }
}
)