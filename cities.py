cityDict=dict()
cityDict['mexico']=['Ecatepec', 'Mexico City','Guadalajara','Juárez','Tijuana','León','Nezahualcóyotl','Monterrey','Zapopan','Naucalpan','Chihuahua','Mérida','Guadalupe','San Luis ','Tlalnepantla','Aguascalientes','Mexicali','Hermosillo','Saltillo]','Acapulco','Morelia','Culiacán','Querétaro','Torreón','Tlaquepaque','Cancún','Chimalhuacan','Reynosa','Tuxtla','Cuautitlán','San Nicolás de los Garza','Ciudad','Toluca','Durango','Veracruz','Matamoros','Ciudad','Xalapa','Tonalá','Mazatlán','Nuevo Laredo','Irapuato','Villahermosa','Cuernavaca','Xico','Celaya','Tampico','Tepic','General Escobedo]','Ixtapaluca','Coacalco','Ciudad Victoria','Ciudad Obregón','PachucaHidalgo','Ensenada','Ciudad Santa Catarina','Oaxaca','Villa ','Gómez Palacio','UruapanMichoacán','Tehuacán','Coatzacoalcos','Los Reyes la Paz','Los Mochis','Soledad de Graciano','Campeche','Monclova','Buenavista','Ciudad Madero','Tapachula','NogalesSonora','La Paz','Puerto Vallarta','Poza Rica','ChicoloapanMéxico','Chilpancingo','MetepecMéxico','Ojo de AguaMéxico','Ciudad del Carmen','San Pablo de las Salinas','Jiutepec','Cuautla','Chalco','Salamanca','San Cristóbal de las Casas','Piedras NegrasCoahuila','San Luis Río Colorado','Chetumal','CórdobaVeracruz','Boca del Río','Zamora de Hidalgo','Acuña','Colima','Zacatecas','San Pedro Garza García','San Juan del Río','Naucalpan','OrizabaVeracruz','Ciudad Valles','Fresnillo','Manzanillo','IgualaGuerrero','MinatitlánVeracruz','DeliciasChihuahua','NavojoaSonora','GuaymasSonora','Hidalgo del Parral','Playa del Carmen']
cityDict['puerto_rico']=['Adjuntas','Aguada','Aguadilla','Aguas Buenas','Aibonito','Añasco','Arecibo','Arroyo','Barceloneta','Barranquitas','Bayamón','Cabo Rojo','Caguas','Camuy','Canóvanas','Carolina','Cataño','Cayey','Ceiba','Ciales','Cidra','Coamo','Comerio','Corozal','Culebra','Dorado','Fajardo','Florida','Guánica','Guayama','Guayanilla','Guaynabo','Gurabo','Hatillo','Hormigueros','Humacao','Isabela','Jayuya','Juana Díaz','Juncos','Lajas','Lares','Las Marías','Las Piedras','Loíza','Luquillo','Manatí','Maricao','Maunabo','Mayagüez','Moca','Morovis','Naguabo','Naranjito','Orocovis','Patillas','Peñuelas','Ponce','Quebradillas','Rincón','Río Grande','Sabana Grande','Salinas','San Germán','San Juan','San Lorenzo','San Sebastián','Santa Isabel','Toa Alta','Toa Baja','Trujillo Alto','Utuado','Vega Alta','Vega Baja','Vieques','Villalba Yabucoa','YaucoAdjuntas','Aguada','Aguadilla','Aguas Buenas','Aibonito','Añasco','Arecibo','Arroyo','Barceloneta','Barranquitas','Bayamón','Cabo Rojo','Caguas','Camuy','Canóvanas','Carolina','Cataño','Cayey','Ceiba','Ciales','Cidra','Coamo','Comerio','Corozal','Culebra','Dorado','Fajardo','Florida','Guánica','Guayama','Guayanilla','Guaynabo','Gurabo','Hatillo','Hormigueros','Humacao','Isabela','Jayuya','Juana Díaz','Juncos','Lajas','Lares','Las Marías','Las Piedras','Loíza','Luquillo','Manatí','Maricao','Maunabo','Mayagüez','Moca','Morovis','Naguabo','Naranjito','Orocovis','Patillas','Peñuelas','Ponce','Quebradillas','Rincón','Río Grande','Sabana Grande','Salinas','San Germán','San Juan','San Lorenzo','San Sebastián','Santa Isabel','Toa Alta','Toa Baja','Trujillo Alto','Utuado','Vega Alta','Vega Baja','Vieques','Villalba Yabucoa','Yauco']
cityDict['brazil']=['São Paulo','Rio de Janeiro','Brasília','Salvador','Fortaleza','Belo Horizonte','Manaus','Curitiba','Recife','Goiânia','Belém','Porto Alegre','Campinas','Guarulhos','São Luís','São Gonçalo','Maceió','Duque de Caxias','Campo Grande','Natal','Teresina','São Bernardo do Campo','Nova Iguaçu','João Pessoa','Santo André','São José dos Campos','Jaboatão dos Guararapes','Osasco','Ribeirão Preto','Uberlândia','Sorocaba','Contagem','Aracaju','Feira de Santana','Cuiabá','Joinville','Aparecida de Goiânia','Juiz de Fora','Londrina','Ananindeua','Porto Velho','Niterói','Belford Roxo','Serra','Caxias do Sul','Campos dos Goytacazes','Macapá','Florianópolis','Vila Velha','São João de Meriti','Mauá','São José do Rio Preto','Mogi das Cruzes','Santos','Betim','Diadema','Maringá','Jundiaí','Campina Grande','Montes Claros','Rio Branco','Piracicaba','Carapicuíba','Olinda','Anápolis','Cariacica','Boa Vista','Bauru','Itaquaquecetuba','Caucaia','São Vicente','Vitória','Caruaru','Blumenau','Franca','Ponta Grossa','Canoas','Petrolina','Pelotas','Vitória da Conquista','Ribeirão das Neves','Uberaba','Paulista','Cascavel','Praia Grande','Guarujá','São José dos Pinhais','Taubaté','Petrópolis','Limeira','Santarém','Suzano','Mossoró','Camaçari','Palmas','Taboão da Serra','Várzea Grande','Santa Maria','Gravataí','Governador Valadares','Sumaré','Marabá','Volta Redonda','Juazeiro do Norte','Barueri','Embu das Artes','Ipatinga','Foz do Iguaçu','Imperatriz','Parnamirim','Viamão','Macaé','São Carlos','Indaiatuba','Novo Hamburgo','Cotia','Magé','São José','Colombo','Itaboraí','Sete Lagoas','Marília','Americana','Juiz de Fora','Volta Redonda','Foz do Iguaçu','Campina Grande','Ipatinga','Taubaté','Campos','Caxias do Sul','São José do Rio Prêto','Piracicaba','Bauru','Montes Claros','Maringá','Itajaí','Pelotas','Itu','Anápolis','Vitória da Conquista','Pôrto Velho','Franca','Blumenau','Ponta Grossa','Limeira','Petrópolis','Crato','Crato','Cabo Frio','Petrolina','Uberaba','Rio Branco','Cascavel','Governador Valadares','Várzea Grande','Santa Maria','Caruaru','Palmas','Boa Vista','Ilhéus','Santarém','Juazeiro do Norte','Itabuna','Imperatriz','Marília','Presidente Prudente','São Carlos','Criciúma','Guaratinguetá','Timon','Mossoró','Sete Lagoas','Divinópolis','Rio Grande','Arapiraca','Cachoeiro de Itapemirim','Rio Claro','Passo Fundo','Nova Friburgo','Araçatuba','Barra Mansa','Marabá','Carpina','Lajes','Dourados','Chapecó','Rio Largo','Barreiras','Sobral','Rondonópolis','Guarapuava','Poços de Caldas','Macaé','Paranaguá','Parnaíba','Castanhal','Jequié','Caxias','Pindamonhangaba','Jaraguá do Sul','Bragança Paulista','Itapetininga','Alagoinhas','Uruguaiana','Pôrto Seguro','Barbacena','Jaú','Pouso Alegre','Botucatu','Santa Cruz do Sul','Conselheiro Lafaiete','Garanhuns','Catanduva','Apucarana','Bagé','Linhares','Barretos','Teófilo Otoni','Passos','Ubá','Ourinhos','Trindade','Arapongas','Araguari','Corumbá','Erechim','Juazeiro','Ponta Porã','Bento Gonçalves','Tatuí','Patos','Itaituba','Tubarão','Muriaé','Itanhaém','Santana do Livramento','Nova Lima','Brusque','Assis','Paulo Afonso','Ituiutaba','Santana','Codó','Araxá','Lavras','Avaré','Formosa','Itumbiara','Abaetetuba','Três Lagoas','São João del Rei','Itaúna','São Mateus','Jataí','São João da Boa Vista','Tucuruí','Campo Mourão','Cachoeira do Sul','Bacabal','Pôrto União','Goiana','Ijuí','Altamira','Paracatu','Iguatu','Paragominas','Guajará-Mirim','Jabuticabal','Balsas','Santa Inês','Rio Negro','Santo Ângelo','Ji-Paraná','Gurupi','Parintins','Curvelo','Caçador','Irecê','Catalão','Vilhena','Valença','Itapeva','Tupã','Fernandópolis','Canela','Piraçununga','Pirapora','Caratinga','Itapetinga','São Borja','Caràzinho','Santa Rosa','Manacapuru','Telêmaco Borba','Guanambi','Ariquemes','Timbaúba','Picos','Arcoverde','Bragança','Cruzeiro do Sul','Serrinha','Vacaria','Janaúba','Formiga','Nova Viçosa','Itapipoca','Estância','São Gabriel','Concórdia','São José de Ribamar','Caicó','Penápolis','Coari','Registro','Camaquã','Crateús','Andradina','Barra do Garças','Batatais','Itacoatiara','Tefé','Araguaína','Quixadá','Barra do Corda','Floriano','Senhor do Bonfim','Rio Verde','Ponte Nova','Guaxupé','Goianésia','Capanema','Itamaraju','Campo Belo','Itaberaba','Breves','Leopoldina','Irati','Cametá','Piripiri','Camocim','Aracati','Inhumas','Imbituba','Araranguá','Canindé','Salgueiro','Penedo','Castro','Brumado','Canoinhas','Jaguaquara','Garça','Palmeira dos Índios','Salinópolis','Frutal','Chapadinha','Aquidauana','Bom Jesus da Lapa','Laguna','Russas','Palmas','Mineiros','Pinheiro','Joaçaba','Remanso','Nanuque','Diamantina','Rosário do Sul','Cristalina','Guaíra','São Francisco do Sul','Açu','Oriximiná','Barreiros','Xique-Xique','Barreirinho','Itapecuru Mirim','Januária','Osório','Morrinhos','Coroatá','Capitão Poço','Maués','Paranaíba','Bocaiúva','São Luís Gonzaga','Campo Maior','Jacareacanga','Barra do Bugres','Tucano','Presidente Dutra','Grajaú','Novo Horizonte','Iturama','Jaguarão','Pontes e Lacerda','Almenara','Tauá','Acaraú','Ubaitaba','Icó','Iporá','Santa Vitória do Palmar','Santa Cruz','Óbidos','Niquelândia','Colíder','Conceição do Araguaia','Aripuanã','Viana','Miracema','Ipu','Canavieiras','Alenquer','Sena Madureira','Granja','Pimenta Bueno','Lapa','São Lourenço do Sul','Colinas','Pires do Rio','Rolim de Moura','Iguape','Jardim','Guanhães','Itambé','Santa Maria da Vitória','Quaraí','Nova Cruz','Maracaju','Baturité','Itaberaí','Araçuaí','Eirunepé','Barras','Manicoré','Portel','Itupiranga','Paracuru','Santa Cruz Cabrália','Viseu','Ceres','Apodi','Fonte Boa','São Gabriel da Cachoeira','Pedreiras','Barcelos','Caracaraí','Alvorada','Porto Nacional','Novo Airão','Sinop','Tocantinópolis','Rosário','Tonantins','Xinguara','Amapá','Abunã','Príncipe da Beira']
cityDict['argentina']=['Buenos Aires','Córdob','Rosario','Mendoza','La Plata','Tucumán','Mar del Plata','Salta','Santa Fe','San Juan','Resistencia','Santiago del Estero','Corrientes','Neuquén','Posadas','San Salvador de Jujuy','Bahía Blanca','Paraná','Formosa','San Fernando del Valle de Catamarca','San Luis','La Rioja','Comodoro Rivadavia','Río Cuarto',]
cityDict['colombia']=['Bogotá','Medellín','Cali','Barranquilla','Bucaramanga','Cartagena','Cúcuta','Soledad','Pereira','Santa Marta','Ibagué','Pasto','Manizales','Villavicencio','Neiva','Armenia','Valledupar','Montería','Sincelejo','Popayán','Buenaventura','Barrancabermeja','Tuluá','Tunja','Cartago','Ríohacha','Ciénaga','Florencia','Girardot','Sogamoso','Pupiales','Duitama','Magangué','Quibdó','Tumaco','Ocaña','Arauca','Sabanalarga','Yopal','El Carmen de Bolívar','Leticia','San Andrés','Garzón','El Banco','Chiquinquirá','Pamplona','Lorica','Turbo','Arjona','Honda','Yarumal','Puerto Berrío','Túquerres','Tame','Tolú','Socorro','Ayapel','Campoalegre','San José del Guaviare','Mocoa','Sonsón','Puerto López','San Marcos','Guapi','Puerto Carreño','Mitú','Orocué','Nuquí','Juradó','San Vicente del Caguán','Inírida']
cityDict['peru']=['Lima','Callao','Arequipa','Trujillo','Chilape','Iquitos','Huancayo','Piura','Cusco','Chimbote','Pucallpa','Tacna','Ica','Juliaca','Ayacucho','Sullana','HuÃ¡nuco','Chincha Alta','Cajamarca','Cerro de Pasco','Puno','Tumbes','Talara','Chosica','Huaraz','Pisco','Huacho','Chulucanas','Puerto Maldonado','Paita','Abancay','Moquegua','Ilo','Tingo MarÃ­a','JaÃ©n','Tarma','FerreÃ±afe','Mollendo','Moyobamba','Huancavelica','Hualmay','Pacasmayo','JuanjuÃ­','Sicuani','Forbe Oroya','Pativilca','Huamachuco','Casma','Tocache Viejo','Chancay','Chachapoyas','Nazca','Sechura','Jauja','CamanÃ¡','Ayaviri','Contamana','Huantachaca','Requena','Huarmey','Ilave','Puerto Pimentel','Satipo','JunÃ­n','San Jacinto','Chota','Lamas','Motupe','Cajabamba','Chilca','Puquio','Santiago','Otuzco','Salaverry','Olmos','Putina','Urubamba','Coracora','Desaguadero','Santo TomÃ¡s','Caballococha','Tarapoto','Tournavista','GÃ¼eppÃ­','Soldado Bartra','Andoas','Puca Urco','Ayacucho','Chiclayo']
cityDict['chile']=['Arica','Iquique','Alto Hospicio','Pozo Almonte','Calama','Tocopilla','Chuquicamata','Taltal','Estación Zaldívar','Mejillones','María Elena','Copiapó','Vallenar','Caldera','Chañaral','El Salvador','Tierra Amarilla','Diego de Almagro','Huasco','La Serena','Ovalle','Illapel','Vicuña','Salamanca','Los Vilos','Andacollo','Combarbalá','El Palqui','Monte Patria','Viña del Mar','Quilpué','Villa Alemana','San Antonio','Quillota','Los Andes','San Felipe','La Calera','Limache','Concón','Quintero','La Ligua','Llay-Llay','Cartagena','Casablanca','Cabildo','Placilla de Peñuelas','La Cruz','Olmué','El Melón','Nogales','El Quisco','Hijuelas','San Esteban','Putaendo','Catemu','Santa María','Las Ventanas','Algarrobo','Rinconada','Calle Larga[note ]','Santo Domingo[note ]','El Tabo[note ]','  RegionPuente Alto','Maipú','La Florida','Las Condes','San Bernardo','Peñalolén','Santiago','Pudahuel','La Pintana','El Bosque','Ñuñoa','Cerro Navia','Recoleta','Renca','Conchalí','La Granja','Estación Central','Quilicura','Providencia','Pedro Aguirre Cerda','Lo Espejo','Macul','Lo Prado','Quinta Normal','San Joaquín','La Reina','San Ramón','La Cisterna','Vitacura','San Miguel','Huechuraba','Lo Barnechea','Cerrillos','Independencia','Peñaflor','Colina','Melipilla','Talagante','Buin','Padre Hurtado','El Monte','Paine','Curacaví','Lampa','Isla de Maipo','La Islita','Bajos de San Agustín','Hospital','Alto Jahuel','San José de Maipo','Tiltil','Pirque[note ]','Rancagua','San Fernando','Rengo','Machalí','Graneros','San Vicente de Tagua Tagua','Santa Cruz','Chimbarongo','Mostazal','Pichilemu','Requínoa','Lo Miranda','Doñihue','Peumo','Nancagua','Las Cabras','Quinta de Tilcoco','Gultro','Codegua','Palmilla[note ]','Talca','Curicó','Linares','Constitución','Cauquenes','Molina','Parral','San Javier','San Clemente','Teno','Longaví','Villa Alegre','Hualañé','Concepción','Talcahuano','Chillán','Los Ángeles','Coronel','Hualpén','Chiguayante','San Pedro de la Paz','Lota','Penco','Tomé','Curanilahue','San Carlos','Mulchén','Nacimiento','Lebu','Cañete','Chillán Viejo','Arauco','La Laja','Hualqui','Los Álamos','Cabrero','Bulnes','Coelemu','Yungay','Yumbel','Quirihue','Quillón','Coihueco','Santa Juana','Santa Bárbara','Huépil','Monte Águila','San Rosendo[note ]','Temuco','Angol','Padre Las Casas','Villarrica','Victoria','Lautaro','Nueva Imperial','Collipulli','Loncoche','Traiguén','Pucón','Pitrufquén','Curacautín','Carahue','Gorbea','Purén','Cunco','Labranza','Freire','Renaico','Valdivia','La Unión','Río Bueno','Panguipulli','Paillaco','Lanco','Mariquina','Futrono','Puerto Montt','Osorno','Castro','Ancud','Puerto Varas','Quellón','Calbuco','Purranque','Llanquihue','Frutillar','Río Negro','Fresia','Los Muermos','Coyhaique','Puerto ','Punta Arenas','Puerto Natales']
cityDict['paraguay']=['Ciudad del Este','San Lorenzo','Luque','Capiatá','Lambaré','Fernando de la Mora','Limpio','Ñemby','EncarnaciónItapúa','Mariano Roque Alonso','Pedro Juan Caballero','Villa Elisa','Caaguazú','Coronel Oviedo','Hernandarias','Presidente Franco','Itauguá','Concepción','Villarrica','San Antonio','Pilar','Caacupé','Itá','Mariscal Estigarribia','Villa Hayes','Minga Guazú','San Ignacio','San Estanislao','Ayolas','Villeta','Areguá']
cityDict['uruguay']=['Montevideo','Salto','Ciudad de la Costa','Paysandú','Las Piedras','Rivera','Maldonado','Tacuarembó','Melo','Mercedes','Artigas','Minas','San José de Mayo','Durazno','Florida,uruguay','Barros Blancos','Ciudad del Plata','San Carlos','Colonia del Sacramento','Pando','Treinta y Tres','Rocha','Fray Bentos','Trinidad','La Paz','Canelones','Carmelo','Dolores','Young','Santa Lucía','Progreso','Paso de Carrasco','Río Branco','Paso de los Toros','Juan Lacaze','Bella Unión','Nueva Helvecia','Libertad','Rosario','Nueva Palmira','Chuy','Punta del Este','Piriápolis','Salinas','Parque del Plata','Lascano','Castillos','Tranqueras','Sarandí del Yí','San Ramón','Tarariras','Pan De Azúcar','Sauce','Sarandí Grande','Atlántida','José Pedro Varela','Tala','Guichón','Cardona','San Jacinto','Toledo','Vergara','Santa Rosa','Florencio Sánchez','La Paloma','San Gregorio de Polanco','Ombúes de Lavalle','Colonia Valdense','Cerrillos','Aiguá','Migues','San Bautista']
cityDict['dr']=['Santo Domingo','San Cristóbal','Santiago','La Vega','San Cristóbal','San Pedro de Macorís','San Francisco de Macorís','La Romana','Higüey','Puerto Plata','Moca']
cityDict['peru']=['Lima','Callao','Arequipa','Trujillo','Chilape','Iquitos','Huancayo','Piura','Cusco','Chimbote','Pucallpa','Tacna','Ica','Juliaca','Ayacucho','Sullana','HuÃ¡nuco','Chincha Alta','Cajamarca','Cerro de Pasco','Puno','Tumbes','Talara','Chosica','Huaraz','Pisco','Huacho','Chulucanas','Puerto Maldonado','Paita','Abancay','Moquegua','Ilo','Tingo MarÃ­a','JaÃ©n','Tarma','FerreÃ±afe','Mollendo','Moyobamba','Huancavelica','Hualmay','Pacasmayo','JuanjuÃ­','Sicuani','Forbe Oroya','Pativilca','Huamachuco','Casma','Tocache Viejo','Chancay','Chachapoyas','Nazca','Sechura','Jauja','CamanÃ¡','Ayaviri','Contamana','Huantachaca','Requena','Huarmey','Ilave','Puerto Pimentel','Satipo','JunÃ­n','San Jacinto','Chota','Lamas','Motupe','Cajabamba','Chilca','Puquio','Santiago','Otuzco','Salaverry','Olmos','Putina','Urubamba','Coracora','Desaguadero','Santo TomÃ¡s','Caballococha','Tarapoto','Tournavista','GÃ¼eppÃ­','Soldado Bartra','Andoas','Puca Urco','Ayacucho','Chiclayo']
cityDict['dominica']=['Atkinson','Barroui','Berekua','Calibishie','Canefield','Castle Bruce','Grand Bay (Berekua)','La Plaine','La Soie (Wesley)','Mahaut','Marigot','Pointe Michel','Portsmouth (Grand-Anse)','Rosalie','Roseau','Saint Joseph','Salisbury','Soufrière','Wesley','Woodford Hill']
cityDict['venezuela']=['Nueva Caracas','Maracaibo','Valencia','Barquisimeto','Maracay','Ciudad Guayana','Barcelona','Cabimas','San Cristóbal','Maturín','Ciudad Bolívar','Cumaná','Maiquetía','Los Teques','Alto Barinas','Acarigua','Punto Fijo','El Tigre','Porlamar','Coro','Valera','Ocumare del Tuy','Guanare','Carora','Carúpano Arriba','San Fernando','Anaco','Calabozo','San Carlos del Zulia','Valle de La Pascua','San Juan de los Morros','San Carlos','San Felipe','Machiques','Upata','Puerto Ayacucho','Tucupita','Trujillo','Zaraza','Altagracia de Orituco','La Asunción','Santa Rita','Guasdalito','Chaguarama','El Dorado','El Manteco','Esmeralda','La Guaira','Barinas','Caracas','Mérida']
cityDict['jamaica']=['Above Rocks','Albert Town','Alexandria','Alligator Pond','Anchovy','Annotto Bay','Balaclava','Bamboo','Bath','Bethel Town','Black River','Bluefields','Bog Walk','Brompton','Brown\'s Town','Buff Bay','Bull Savanna','Cambridge','Cascade','Cave Valley','Chapelton','Christiana','Claremont','Clark\'s Town','Coleyville','Constant Spring','Croft\'s Hill','Dalvey','Darliston','Discovery Bay ','Duncans','Easington','Ewarton','Falmouth','Frankfield','Frome','Gayle','Golden Grove','Gordon Town','Grange Hill','Green Island','Guy\'s Hill','Hayes','Highgate','Hope Bay','Hopewell','Islington','Kellits','Lacovia','Linstead','Lionel Town','Little London','Lluidas Vale','Lucea','Lucky Hill','Maggotty','Malvern','Manchioneal','Maroon Town','Mavis Bank','Moneague','Moore Town','Morant Bay','Nain','Negril','Ocho Rios','Old Harbour','Old Harbour Bay','Oracabessa','Osbourne Store','Petersfield','Point Hill','Port Antonio','Port Maria','Porus','Race Course','Richmond','Rio Bueno','Riversdale','Rocky Point','Runaway Bay','Saint Ann\'s Bay','Sandy Bay','Sanguinetti','Santa Cruz','Savanna','Seaford Town','Seaforth','Siloah','Southfield','Spalding','Stony Hill','Trinity Ville','Ulster Spring','Wakefield','White House','Williamsfield','Yallahs']
cityDict['ecuador']=['Ambato','Arajuno','Babahoyo','Bahía de Caráquez','Baños de Agua Santa','Cuenca','Durán','Esmeraldas','Guaranda','Guayaquil','Ibarra','La Libertad','Latacunga','Loja','Macas','Machala','Manta','Milagro','Nueva Loja','Portoviejo','Piñas','Pintag','Quevedo','Quito']
cityDict['costa rica']=['Aguacaliente (San Francisco)','Alajuela','Alajuelita','Aserri','Barranca','Calle Blancos','Canas','Carmen','Cartago','Cinco Esquinas','Concepcion','Curridabat','Desamparados','Gravilias','Guadalupe','Guapiles','Heredia','Ipis','Liberia','Limon (Puerto Limon)','Mata de Platano','Mercedes','Nicoya','Paraiso','Patalillo','Patarra','Puntarenas','Purral','Quesada','San Antonio','San Diego','San Felipe','San Francisco','San Isidro','San Isidro de El General','San Jose','San Jose de Alajuela','San Juan (San Juan de Tibas)','San Juan de Dios','San Miguel','San Nicolas','San Pablo','San Pedro','San Rafael','San Rafael Abajo','San Vicente','Siquirres','Tejar','Tirrases','Turrialba','Ulloa (Barrial)',]
cityDict['cuba']=['Havana','Santiago de Cuba','CamagÃ¼ey','HolguÃ­n','GuantÃ¡namo','Santa Clara','Las Tunas','Bayamo','Pinar del RÃ­o','Cienfuegos','Matanzas','Ciego de Ãvila','Manzanillo','Sancti SpÃ­ritus','Palma Soriano','GÃ¼ines','Artemisa','MorÃ³n','ColÃ³n','Sagua la Grande','Placetas','Nuevitas','Banes','San Antonio de los BaÃ±os','CaibariÃ©n','Nueva Gerona','San Luis','San Luis','RÃ­o Cauto','Primero de Enero','Bolivia','Guanajay','Niquero','Gaspar','Jaruco','Los Palacios','Majagua','Cubitas','QuivicÃ¡n','Esmeralda','Venezuela','Ciro Redondo','San JosÃ© de las Lajas','Bejucal','ImÃ­as','MayarÃ­','Campechuela','JagÃ¼ey Grande','Lajas','Trinidad','BÃ¡guanos','Palmira','Santa LucÃ­a','Puerto Padre','Florida','Corralillo','Baracoa','San CristÃ³bal','Manicaragua','Minas','San GermÃ¡n','Moa','Los Arabos','Cayo MambÃ­','Ranchuelo','MartÃ­','ConsolaciÃ³n del Sur','Gibara','Sagua de TÃ¡namo','Caimito','Jobabo','Limonar','San Antonio del Sur','BahÃ­a Honda','Remedios','CabaiguÃ¡n','BartolomÃ© MasÃ³','ManatÃ­','Vertientes','CamajuanÃ­','Pedro Betancourt','Contramaestre','GÃ¼ira de Melena','Mariel','JesÃºs MenÃ©ndez','Nueva Paz','Perico','La Sierpe','Jatibonico','Najasa','Aguada de Pasajeros','Florencia','San NicolÃ¡s','Buey Arriba','San Juan y MartÃ­nez','Palenque','Madruga','PilÃ³n','Colombia','Quemado de GÃ¼ines','Bauta','Cacocum','Rodas','Melena del Sur','JiguanÃ­','GuÃ¡imaro','Cifuentes','Calixto','Calimete','La MÃ¡quina','Yara','Chambas','Antilla','Guisa','Encrucijada','La Palma','UniÃ³n de Reyes','Minas de Matahambre','Santa Cruz del Norte','Cumanayagua','CÃ¡rdenas','Yaguajay','Jovellanos','SibanicÃº','Santo Domingo','AlquÃ­zar','Media Luna','Taguasco','JimaguayÃº','Santa Cruz del Sur','Fomento','BatabanÃ³','Amancio','ViÃ±ales','Carlos Manuel de CÃ©spedes','Cruces','Candelaria']
cityDict['bolivia']=['Sant\'a Cruz','La Paz','Cochabamba','Oruro','Quillacollo','Sucre','Potosí','Tarija','Montero','Trinidad','Riberalta','Cobija','Villazón','Bermejo','Guayaramerín','Viacha','Tupiza','Llallagua','Camiri','Punata','San Ignacio de Velasco','Puerto Suárez','San Borja','Villamontes','Cliza','Ascensión','Uyuni','Rurrenabaque','Portachuelo','Puerto Quijarro','Roboré','Challapata','Avichaca','Vallegrande','Aiquile','Reyes','San Ramón','San Carlos','San Matías','Betanzos','Uncia','Camargo','San Javier','Apolo','Quime','Charagua','San Lorenzo','Samaipata','Padilla','Entre Ríos','Tarabuco','Baures','Coroico','Sorata','Corocoro','Puerto Villarroel','San Rafael','Puerto Acosta','Sicasica','Cuevo','Sabaya','Llica','Charaña','Piso Firme','Puerto Heath','Santa Cruz de la Sierra']




mexico=['Ecatepec', 'Mexico City','Guadalajara','Juárez','Tijuana','León','Nezahualcóyotl','Monterrey','Zapopan','Naucalpan','Chihuahua','Mérida','Guadalupe','San Luis ','Tlalnepantla','Aguascalientes','Mexicali','Hermosillo','Saltillo]','Acapulco','Morelia','Culiacán','Querétaro','Torreón','Tlaquepaque','Cancún','Chimalhuacan','Reynosa','Tuxtla','Cuautitlán','San Nicolás de los Garza','Ciudad','Toluca','Durango','Veracruz','Matamoros','Ciudad','Xalapa','Tonalá','Mazatlán','Nuevo Laredo','Irapuato','Villahermosa','Cuernavaca','Xico','Celaya','Tampico','Tepic','General Escobedo]','Ixtapaluca','Coacalco','Ciudad Victoria','Ciudad Obregón','PachucaHidalgo','Ensenada','Ciudad Santa Catarina','Oaxaca','Villa ','Gómez Palacio','UruapanMichoacán','Tehuacán','Coatzacoalcos','Los Reyes la Paz','Los Mochis','Soledad de Graciano','Campeche','Monclova','Buenavista','Ciudad Madero','Tapachula','NogalesSonora','La Paz','Puerto Vallarta','Poza Rica','ChicoloapanMéxico','Chilpancingo','MetepecMéxico','Ojo de AguaMéxico','Ciudad del Carmen','San Pablo de las Salinas','Jiutepec','Cuautla','Chalco','Salamanca','San Cristóbal de las Casas','Piedras NegrasCoahuila','San Luis Río Colorado','Chetumal','CórdobaVeracruz','Boca del Río','Zamora de Hidalgo','Acuña','Colima','Zacatecas','San Pedro Garza García','San Juan del Río','Naucalpan','OrizabaVeracruz','Ciudad Valles','Fresnillo','Manzanillo','IgualaGuerrero','MinatitlánVeracruz','DeliciasChihuahua','NavojoaSonora','GuaymasSonora','Hidalgo del Parral','Playa del Carmen']
puerto_ricco=['Adjuntas','Aguada','Aguadilla','Aguas Buenas','Aibonito','Añasco','Arecibo','Arroyo','Barceloneta','Barranquitas','Bayamón','Cabo Rojo','Caguas','Camuy','Canóvanas','Carolina','Cataño','Cayey','Ceiba','Ciales','Cidra','Coamo','Comerio','Corozal','Culebra','Dorado','Fajardo','Florida','Guánica','Guayama','Guayanilla','Guaynabo','Gurabo','Hatillo','Hormigueros','Humacao','Isabela','Jayuya','Juana Díaz','Juncos','Lajas','Lares','Las Marías','Las Piedras','Loíza','Luquillo','Manatí','Maricao','Maunabo','Mayagüez','Moca','Morovis','Naguabo','Naranjito','Orocovis','Patillas','Peñuelas','Ponce','Quebradillas','Rincón','Río Grande','Sabana Grande','Salinas','San Germán','San Juan','San Lorenzo','San Sebastián','Santa Isabel','Toa Alta','Toa Baja','Trujillo Alto','Utuado','Vega Alta','Vega Baja','Vieques','Villalba Yabucoa','YaucoAdjuntas','Aguada','Aguadilla','Aguas Buenas','Aibonito','Añasco','Arecibo','Arroyo','Barceloneta','Barranquitas','Bayamón','Cabo Rojo','Caguas','Camuy','Canóvanas','Carolina','Cataño','Cayey','Ceiba','Ciales','Cidra','Coamo','Comerio','Corozal','Culebra','Dorado','Fajardo','Florida','Guánica','Guayama','Guayanilla','Guaynabo','Gurabo','Hatillo','Hormigueros','Humacao','Isabela','Jayuya','Juana Díaz','Juncos','Lajas','Lares','Las Marías','Las Piedras','Loíza','Luquillo','Manatí','Maricao','Maunabo','Mayagüez','Moca','Morovis','Naguabo','Naranjito','Orocovis','Patillas','Peñuelas','Ponce','Quebradillas','Rincón','Río Grande','Sabana Grande','Salinas','San Germán','San Juan','San Lorenzo','San Sebastián','Santa Isabel','Toa Alta','Toa Baja','Trujillo Alto','Utuado','Vega Alta','Vega Baja','Vieques','Villalba Yabucoa','Yauco']
brazil=['São Paulo','Rio de Janeiro','Brasília','Salvador','Fortaleza','Belo Horizonte','Manaus','Curitiba','Recife','Goiânia','Belém','Porto Alegre','Campinas','Guarulhos','São Luís','São Gonçalo','Maceió','Duque de Caxias','Campo Grande','Natal','Teresina','São Bernardo do Campo','Nova Iguaçu','João Pessoa','Santo André','São José dos Campos','Jaboatão dos Guararapes','Osasco','Ribeirão Preto','Uberlândia','Sorocaba','Contagem','Aracaju','Feira de Santana','Cuiabá','Joinville','Aparecida de Goiânia','Juiz de Fora','Londrina','Ananindeua','Porto Velho','Niterói','Belford Roxo','Serra','Caxias do Sul','Campos dos Goytacazes','Macapá','Florianópolis','Vila Velha','São João de Meriti','Mauá','São José do Rio Preto','Mogi das Cruzes','Santos','Betim','Diadema','Maringá','Jundiaí','Campina Grande','Montes Claros','Rio Branco','Piracicaba','Carapicuíba','Olinda','Anápolis','Cariacica','Boa Vista','Bauru','Itaquaquecetuba','Caucaia','São Vicente','Vitória','Caruaru','Blumenau','Franca','Ponta Grossa','Canoas','Petrolina','Pelotas','Vitória da Conquista','Ribeirão das Neves','Uberaba','Paulista','Cascavel','Praia Grande','Guarujá','São José dos Pinhais','Taubaté','Petrópolis','Limeira','Santarém','Suzano','Mossoró','Camaçari','Palmas','Taboão da Serra','Várzea Grande','Santa Maria','Gravataí','Governador Valadares','Sumaré','Marabá','Volta Redonda','Juazeiro do Norte','Barueri','Embu das Artes','Ipatinga','Foz do Iguaçu','Imperatriz','Parnamirim','Viamão','Macaé','São Carlos','Indaiatuba','Novo Hamburgo','Cotia','Magé','São José','Colombo','Itaboraí','Sete Lagoas','Marília','Americana','Juiz de Fora','Volta Redonda','Foz do Iguaçu','Campina Grande','Ipatinga','Taubaté','Campos','Caxias do Sul','São José do Rio Prêto','Piracicaba','Bauru','Montes Claros','Maringá','Itajaí','Pelotas','Itu','Anápolis','Vitória da Conquista','Pôrto Velho','Franca','Blumenau','Ponta Grossa','Limeira','Petrópolis','Crato','Crato','Cabo Frio','Petrolina','Uberaba','Rio Branco','Cascavel','Governador Valadares','Várzea Grande','Santa Maria','Caruaru','Palmas','Boa Vista','Ilhéus','Santarém','Juazeiro do Norte','Itabuna','Imperatriz','Marília','Presidente Prudente','São Carlos','Criciúma','Guaratinguetá','Timon','Mossoró','Sete Lagoas','Divinópolis','Rio Grande','Arapiraca','Cachoeiro de Itapemirim','Rio Claro','Passo Fundo','Nova Friburgo','Araçatuba','Barra Mansa','Marabá','Carpina','Lajes','Dourados','Chapecó','Rio Largo','Barreiras','Sobral','Rondonópolis','Guarapuava','Poços de Caldas','Macaé','Paranaguá','Parnaíba','Castanhal','Jequié','Caxias','Pindamonhangaba','Jaraguá do Sul','Bragança Paulista','Itapetininga','Alagoinhas','Uruguaiana','Pôrto Seguro','Barbacena','Jaú','Pouso Alegre','Botucatu','Santa Cruz do Sul','Conselheiro Lafaiete','Garanhuns','Catanduva','Apucarana','Bagé','Linhares','Barretos','Teófilo Otoni','Passos','Ubá','Ourinhos','Trindade','Arapongas','Araguari','Corumbá','Erechim','Juazeiro','Ponta Porã','Bento Gonçalves','Tatuí','Patos','Itaituba','Tubarão','Muriaé','Itanhaém','Santana do Livramento','Nova Lima','Brusque','Assis','Paulo Afonso','Ituiutaba','Santana','Codó','Araxá','Lavras','Avaré','Formosa','Itumbiara','Abaetetuba','Três Lagoas','São João del Rei','Itaúna','São Mateus','Jataí','São João da Boa Vista','Tucuruí','Campo Mourão','Cachoeira do Sul','Bacabal','Pôrto União','Goiana','Ijuí','Altamira','Paracatu','Iguatu','Paragominas','Guajará-Mirim','Jabuticabal','Balsas','Santa Inês','Rio Negro','Santo Ângelo','Ji-Paraná','Gurupi','Parintins','Curvelo','Caçador','Irecê','Catalão','Vilhena','Valença','Itapeva','Tupã','Fernandópolis','Canela','Piraçununga','Pirapora','Caratinga','Itapetinga','São Borja','Caràzinho','Santa Rosa','Manacapuru','Telêmaco Borba','Guanambi','Ariquemes','Timbaúba','Picos','Arcoverde','Bragança','Cruzeiro do Sul','Serrinha','Vacaria','Janaúba','Formiga','Nova Viçosa','Itapipoca','Estância','São Gabriel','Concórdia','São José de Ribamar','Caicó','Penápolis','Coari','Registro','Camaquã','Crateús','Andradina','Barra do Garças','Batatais','Itacoatiara','Tefé','Araguaína','Quixadá','Barra do Corda','Floriano','Senhor do Bonfim','Rio Verde','Ponte Nova','Guaxupé','Goianésia','Capanema','Itamaraju','Campo Belo','Itaberaba','Breves','Leopoldina','Irati','Cametá','Piripiri','Camocim','Aracati','Inhumas','Imbituba','Araranguá','Canindé','Salgueiro','Penedo','Castro','Brumado','Canoinhas','Jaguaquara','Garça','Palmeira dos Índios','Salinópolis','Frutal','Chapadinha','Aquidauana','Bom Jesus da Lapa','Laguna','Russas','Palmas','Mineiros','Pinheiro','Joaçaba','Remanso','Nanuque','Diamantina','Rosário do Sul','Cristalina','Guaíra','São Francisco do Sul','Açu','Oriximiná','Barreiros','Xique-Xique','Barreirinho','Itapecuru Mirim','Januária','Osório','Morrinhos','Coroatá','Capitão Poço','Maués','Paranaíba','Bocaiúva','São Luís Gonzaga','Campo Maior','Jacareacanga','Barra do Bugres','Tucano','Presidente Dutra','Grajaú','Novo Horizonte','Iturama','Jaguarão','Pontes e Lacerda','Almenara','Tauá','Acaraú','Ubaitaba','Icó','Iporá','Santa Vitória do Palmar','Santa Cruz','Óbidos','Niquelândia','Colíder','Conceição do Araguaia','Aripuanã','Viana','Miracema','Ipu','Canavieiras','Alenquer','Sena Madureira','Granja','Pimenta Bueno','Lapa','São Lourenço do Sul','Colinas','Pires do Rio','Rolim de Moura','Iguape','Jardim','Guanhães','Itambé','Santa Maria da Vitória','Quaraí','Nova Cruz','Maracaju','Baturité','Itaberaí','Araçuaí','Eirunepé','Barras','Manicoré','Portel','Itupiranga','Paracuru','Santa Cruz Cabrália','Viseu','Ceres','Apodi','Fonte Boa','São Gabriel da Cachoeira','Pedreiras','Barcelos','Caracaraí','Alvorada','Porto Nacional','Novo Airão','Sinop','Tocantinópolis','Rosário','Tonantins','Xinguara','Amapá','Abunã','Príncipe da Beira']
argentina=['Buenos Aires','Córdob','Rosario','Mendoza','La Plata','Tucumán','Mar del Plata','Salta','Santa Fe','San Juan','Resistencia','Santiago del Estero','Corrientes','Neuquén','Posadas','San Salvador de Jujuy','Bahía Blanca','Paraná','Formosa','San Fernando del Valle de Catamarca','San Luis','La Rioja','Comodoro Rivadavia','Río Cuarto',]
cities=['miami']
columbia=['Bogotá','Medellín','Cali','Barranquilla','Bucaramanga','Cartagena','Cúcuta','Soledad','Pereira','Santa Marta','Ibagué','Pasto','Manizales','Villavicencio','Neiva','Armenia','Valledupar','Montería','Sincelejo','Popayán','Buenaventura','Barrancabermeja','Tuluá','Tunja','Cartago','Ríohacha','Ciénaga','Florencia','Girardot','Sogamoso','Pupiales','Duitama','Magangué','Quibdó','Tumaco','Ocaña','Arauca','Sabanalarga','Yopal','El Carmen de Bolívar','Leticia','San Andrés','Garzón','El Banco','Chiquinquirá','Pamplona','Lorica','Turbo','Arjona','Honda','Yarumal','Puerto Berrío','Túquerres','Tame','Tolú','Socorro','Ayapel','Campoalegre','San José del Guaviare','Mocoa','Sonsón','Puerto López','San Marcos','Guapi','Puerto Carreño','Mitú','Orocué','Nuquí','Juradó','San Vicente del Caguán','Inírida']
peru=['Lima','Callao','Arequipa','Trujillo','Chilape','Iquitos','Huancayo','Piura','Cusco','Chimbote','Pucallpa','Tacna','Ica','Juliaca','Ayacucho','Sullana','HuÃ¡nuco','Chincha Alta','Cajamarca','Cerro de Pasco','Puno','Tumbes','Talara','Chosica','Huaraz','Pisco','Huacho','Chulucanas','Puerto Maldonado','Paita','Abancay','Moquegua','Ilo','Tingo MarÃ­a','JaÃ©n','Tarma','FerreÃ±afe','Mollendo','Moyobamba','Huancavelica','Hualmay','Pacasmayo','JuanjuÃ­','Sicuani','Forbe Oroya','Pativilca','Huamachuco','Casma','Tocache Viejo','Chancay','Chachapoyas','Nazca','Sechura','Jauja','CamanÃ¡','Ayaviri','Contamana','Huantachaca','Requena','Huarmey','Ilave','Puerto Pimentel','Satipo','JunÃ­n','San Jacinto','Chota','Lamas','Motupe','Cajabamba','Chilca','Puquio','Santiago','Otuzco','Salaverry','Olmos','Putina','Urubamba','Coracora','Desaguadero','Santo TomÃ¡s','Caballococha','Tarapoto','Tournavista','GÃ¼eppÃ­','Soldado Bartra','Andoas','Puca Urco','Ayacucho','Chiclayo']
chile=['Arica','Iquique','Alto Hospicio','Pozo Almonte','Calama','Tocopilla','Chuquicamata','Taltal','Estación Zaldívar','Mejillones','María Elena','Copiapó','Vallenar','Caldera','Chañaral','El Salvador','Tierra Amarilla','Diego de Almagro','Huasco','La Serena','Ovalle','Illapel','Vicuña','Salamanca','Los Vilos','Andacollo','Combarbalá','El Palqui','Monte Patria','Viña del Mar','Quilpué','Villa Alemana','San Antonio','Quillota','Los Andes','San Felipe','La Calera','Limache','Concón','Quintero','La Ligua','Llay-Llay','Cartagena','Casablanca','Cabildo','Placilla de Peñuelas','La Cruz','Olmué','El Melón','Nogales','El Quisco','Hijuelas','San Esteban','Putaendo','Catemu','Santa María','Las Ventanas','Algarrobo','Rinconada','Calle Larga[note ]','Santo Domingo[note ]','El Tabo[note ]','  RegionPuente Alto','Maipú','La Florida','Las Condes','San Bernardo','Peñalolén','Santiago','Pudahuel','La Pintana','El Bosque','Ñuñoa','Cerro Navia','Recoleta','Renca','Conchalí','La Granja','Estación Central','Quilicura','Providencia','Pedro Aguirre Cerda','Lo Espejo','Macul','Lo Prado','Quinta Normal','San Joaquín','La Reina','San Ramón','La Cisterna','Vitacura','San Miguel','Huechuraba','Lo Barnechea','Cerrillos','Independencia','Peñaflor','Colina','Melipilla','Talagante','Buin','Padre Hurtado','El Monte','Paine','Curacaví','Lampa','Isla de Maipo','La Islita','Bajos de San Agustín','Hospital','Alto Jahuel','San José de Maipo','Tiltil','Pirque[note ]','Rancagua','San Fernando','Rengo','Machalí','Graneros','San Vicente de Tagua Tagua','Santa Cruz','Chimbarongo','Mostazal','Pichilemu','Requínoa','Lo Miranda','Doñihue','Peumo','Nancagua','Las Cabras','Quinta de Tilcoco','Gultro','Codegua','Palmilla[note ]','Talca','Curicó','Linares','Constitución','Cauquenes','Molina','Parral','San Javier','San Clemente','Teno','Longaví','Villa Alegre','Hualañé','Concepción','Talcahuano','Chillán','Los Ángeles','Coronel','Hualpén','Chiguayante','San Pedro de la Paz','Lota','Penco','Tomé','Curanilahue','San Carlos','Mulchén','Nacimiento','Lebu','Cañete','Chillán Viejo','Arauco','La Laja','Hualqui','Los Álamos','Cabrero','Bulnes','Coelemu','Yungay','Yumbel','Quirihue','Quillón','Coihueco','Santa Juana','Santa Bárbara','Huépil','Monte Águila','San Rosendo[note ]','Temuco','Angol','Padre Las Casas','Villarrica','Victoria','Lautaro','Nueva Imperial','Collipulli','Loncoche','Traiguén','Pucón','Pitrufquén','Curacautín','Carahue','Gorbea','Purén','Cunco','Labranza','Freire','Renaico','Valdivia','La Unión','Río Bueno','Panguipulli','Paillaco','Lanco','Mariquina','Futrono','Puerto Montt','Osorno','Castro','Ancud','Puerto Varas','Quellón','Calbuco','Purranque','Llanquihue','Frutillar','Río Negro','Fresia','Los Muermos','Coyhaique','Puerto ','Punta Arenas','Puerto Natales']
paraguay=['Ciudad del Este','San Lorenzo','Luque','Capiatá','Lambaré','Fernando de la Mora','Limpio','Ñemby','EncarnaciónItapúa','Mariano Roque Alonso','Pedro Juan Caballero','Villa Elisa','Caaguazú','Coronel Oviedo','Hernandarias','Presidente Franco','Itauguá','Concepción','Villarrica','San Antonio','Pilar','Caacupé','Itá','Mariscal Estigarribia','Villa Hayes','Minga Guazú','San Ignacio','San Estanislao','Ayolas','Villeta','Areguá']
uruguay=['Montevideo','Salto','Ciudad de la Costa','Paysandú','Las Piedras','Rivera','Maldonado','Tacuarembó','Melo','Mercedes','Artigas','Minas','San José de Mayo','Durazno','Florida','Barros Blancos','Ciudad del Plata','San Carlos','Colonia del Sacramento','Pando','Treinta y Tres','Rocha','Fray Bentos','Trinidad','La Paz','Canelones','Carmelo','Dolores','Young','Santa Lucía','Progreso','Paso de Carrasco','Río Branco','Paso de los Toros','Juan Lacaze','Bella Unión','Nueva Helvecia','Libertad','Rosario','Nueva Palmira','Chuy','Punta del Este','Piriápolis','Salinas','Parque del Plata','Lascano','Castillos','Tranqueras','Sarandí del Yí','San Ramón','Tarariras','Pan De Azúcar','Sauce','Sarandí Grande','Atlántida','José Pedro Varela','Tala','Guichón','Cardona','San Jacinto','Toledo','Vergara','Santa Rosa','Florencio Sánchez','La Paloma','San Gregorio de Polanco','Ombúes de Lavalle','Colonia Valdense','Cerrillos','Aiguá','Migues','San Bautista']
