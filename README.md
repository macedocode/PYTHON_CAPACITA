                                     ---------------PARKING_SERVICE----------------
Descrição

Sistema de gerenciamento de estacionamento desenvolvido utilizando Python com framework Django, com objetivo de oferecer uma solução versátil e de alta performance, projetada para se adaptar à realidade de pequenos e grandes estacionamentos

Estrutura do Sistema

O modelo Customer representa os clientes do sistema. Ele possui informações como nome, CPF, telefone e está relacionado ao usuário do Django através de um relacionamento OneToOne.

Vehicle

O modelo Vehicle representa os veículos cadastrados, contendo placa, marca, modelo, cor, tipo de veículo e o proprietário.

VehicleType

Esse modelo define os tipos de veículos, como carro e moto.

ParkingSpot

O modelo ParkingSpot representa as vagas do estacionamento. Cada vaga possui um número único e um status indicando se está ocupada ou livre.
ParkingRecord
O ParkingRecord registra a entrada e saída dos veículos no estacionamento, relacionando um veículo a uma vaga e armazenando os horários de entrada e saída.

Foi implementado um signal que atualiza automaticamente o status da vaga. Quando um registro é criado ou atualizado, a vaga é marcada como ocupada ou livre dependendo se o veículo ainda está no estacionamento.

Django Admin

Utilizei o Django Admin para gerenciar os dados do sistema, permitindo 

Cadastra um cliente

Cadastra um veículo vinculado ao cliente

Cria vagas no estacionamento

Registra entrada do veículo (ParkingRecord)

Sistema marca a vaga como ocupada automaticamente

Quando define horário de saída, a vaga é liberada.

 Como executar o Sistema
python manage.py migrate
python manage.py runserver

Acesse:
http://127.0.0.1:8000/admin

Projeto acadêmico.



![Menu Principal](https://github.com/user-attachments/assets/9db16d0e-cb60-475b-a5f6-730b4a58a9b9)




<img width="1365" height="607" alt="clientes" src="https://github.com/user-attachments/assets/ce78b001-60a4-423b-96ef-e9930e93f3eb" />


![deletar clientes](https://github.com/user-attachments/assets/3c76c3df-58b3-4f68-8fc0-917c2592a61b)

<img width="1343" height="662" alt="add clientes" src="https://github.com/user-attachments/assets/3d9f95b3-2824-48e2-a46e-6f68a2495bfb" />


<img width="1349" height="613" alt="vagas" src="https://github.com/user-attachments/assets/381ab0f0-2905-4c93-befb-bd26b3774cc3" />







<img width="1337" height="601" alt="tipos de veiculos" src="https://github.com/user-attachments/assets/3603d11a-b09f-4162-9909-820bf58f532a" />


<img width="1341" height="602" alt="registros da entrada do veiculo" src="https://github.com/user-attachments/assets/aeaaa07a-2004-46d5-bc18-66396b94efba" />



<img width="1335" height="641" alt="registros do estacionament" src="https://github.com/user-attachments/assets/585602cd-da78-4c26-92e4-c735f47072b6" />
















