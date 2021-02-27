import json
import os

file_arr = [os.path.join(r,file) for r,d,f in os.walk(".") for file in f if file.endswith(".json")]
messageList = []
for filePath in file_arr:

	with open(filePath,encoding="utf8") as f:
		data = json.load(f)
	
	messageList.append(data)

message = json.dumps(messageList)

with open("profile.json",encoding="utf8") as f:
	profile = json.load(f)

profile = json.dumps(profile)




result = '''
var app = angular.module('myApp', []);

app.controller('myController', function($scope,$http){
		$scope.showProfile = true;

		$scope.fetchMessages = function(){
            
                                    $scope.messages = '''+message+''';
        };
		$scope.fetchProfile = function(){
				
              
                                    $scope.profile = '''+profile+''';
                             
          };


		$scope.openChat = function(message){
			$scope.showProfile= false;
			$scope.activeChat = message;	
			//$scope.activeChat.messages.prevDate = message.messages[message.messages.length-1].created_at;
			setInterval($scope.updateScroll,2000);
		}
		$scope.writeDate = function(newDate){
			if(!$scope.activeChat.messages.prevDate){
				$scope.activeChat.messages.prevDate = newDate;
				return true;
			}
			else if($scope.activeChat.messages.prevDate==newDate){
				return true;
			}
			else if($scope.days($scope.activeChat.messages.prevDate,newDate)>1){
				$scope.activeChat.messages.prevDate = newDate;
				return true;
			}
			else{
				
				return false;
			}
		};
		$scope.days = function(date1,date2) {
				
			var date2 = new Date(date2);
			var date1 = new Date(date1);
			var timeDiff = Math.abs(date2.getTime() - date1.getTime());
			$scope.dayDifference = Math.ceil(timeDiff / (1000 * 3600 * 24));
			return $scope.dayDifference;
		}
		
		$scope.updateScroll = function(){
			var element = document.getElementById("activeWindow");
			element.scrollBottom = element.scrollHeight;
		}
		$scope.fetchProfile();
		$scope.fetchMessages();



		
});
'''


with open('script.js', 'w',encoding="utf8") as json_file:
	json_file.write(result)


#print([os.path.join(r,file) for r,d,f in os.walk(".") for file in f if file.endswith(".json")])  
	
	