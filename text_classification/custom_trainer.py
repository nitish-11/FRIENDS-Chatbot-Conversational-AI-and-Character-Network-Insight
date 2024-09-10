# import torch
# from torch import nn
# from transformers import Trainer 

# class CustomTrainer(Trainer):
#     def compute_loss(self,model,inputs,return_outputs=False):
#         labels = inputs.get("labels")

#         # Forward Pass
#         outputs = model(**inputs)
#         logits = outputs.get("logits")
#         logits = logits.float()
        
#         # Compute Custom Loss
#         loss_fct = nn.CrossEntropyLoss(weight = torch.tensor(self.class_weights, dtype=torch.float).to(device=self.device))
#         loss = loss_fct(logits.view(-1, self.model.config.num_labels ),labels.view(-1))
#         return (loss,outputs) if return_outputs else loss

#     def set_class_weights(self,class_weights):
#         self.class_weights = class_weights
    
#     def set_device(self,device):
#         self.device = device



import torch
from torch import nn
from transformers import Trainer

class CustomTrainer(Trainer):
    def compute_loss(self, model, inputs, return_outputs=False):
        labels = inputs.get("labels")

        # Forward Pass
        outputs = model(**inputs)
        logits = outputs.get("logits").float()
        
        # Ensure the model's device is used if device is not set
        if not hasattr(self, 'device'):
            self.device = model.device

        # Compute Custom Loss
        loss_fct = nn.CrossEntropyLoss(
            weight=torch.tensor(self.class_weights, dtype=torch.float).to(self.device)
        )
        loss = loss_fct(logits.view(-1, self.model.config.num_labels), labels.view(-1))
        
        return (loss, outputs) if return_outputs else loss

    def set_class_weights(self, class_weights):
        """Set class weights for imbalanced datasets."""
        self.class_weights = class_weights
    
    def set_device(self, device=None):
        """Set the device, default to the model's device if not provided."""
        if device is None:
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.device = device
