function guessv2(v1, seen,round, assignment, truth, update_diff, predicted_condition) {
   const url = "guess";

   var d1 = document.getElementById("diagnosis").value.toLowerCase();
   var d2 = document.getElementById("diagnosis2").value.toLowerCase();
   var d3 = document.getElementById("diagnosis3").value.toLowerCase();

  
  
   $(':button').prop('disabled', true);

      document.getElementById("submission").disabled = true;
      document.getElementById("submission").style.display = "none";
      document.getElementById("dataentry").style.display = "none";
      document.getElementById("aiprediction").style.display = "none";
      
      
      document.getElementById("question").style.display = "none";
      // document.getElementById("question2").style.display = "none";
      document.getElementById("dataentry").style.display = "none";
      if ($(document).width() >580) {
      document.getElementById("groundtruth").style.display = "inline";
    }
      
      document.getElementById("next").disabled = false;
      document.getElementById("next").style.display = "block";
      document.getElementById("next2").disabled = false;
      document.getElementById("next2").style.display = "block";
      document.getElementById("common-miss").style.display = "block";
    
   
   


    var refDict={};
    referrals=document.getElementsByClassName("referral");
    for (var ele = 0; ele<referrals.length; ele++) {
        if (referrals[ele].checked==true) {
            refDict[referrals[ele].getAttribute("name")]=1;
        }
        else{
            refDict[referrals[ele].getAttribute("name")]=0;
        }        
    }

$.ajax({
            url: url,
            method: 'post',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify({
                'image': v1,
                'guess': d1, 
                'guess_int': document.getElementById("myRange").value,
                'correct': 1,
                'round':round,
                'differential2': d2,
                'differential3': d3,
                'seen': seen,
                'assignment': assignment,
                'biopsy':  refDict['biopsy'],
                'dermatologist': refDict['dermatologist'],


            }),
            error: function(data) {
                console.log(data);
            },
            success: function(data) {
                console.log(data)
            }
        });
    }