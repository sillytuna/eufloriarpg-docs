
Seed Class
==========



Namespace
    :dn:ns:`Clay.Game.Mod.Entities`

Assemblies
    * Clay.Game

----

.. contents::
   :local:



Inheritance Hierarchy
---------------------

* :dn:cls:`System.Object`
* :dn:cls:`Tuna.Mob`
* :dn:cls:`Clay.Game.Mod.Entities.Entity`
* :dn:cls:`Clay.Game.Mod.Entities.Vehicle`
* :dn:cls:`Clay.Game.Mod.Entities.Equipment`
* :dn:cls:`Clay.Game.Mod.Entities.Seed`




Syntax
------

.. code-block:: csharp

    public class Seed : Equipment, IComparable, IAudioSourceInfo, ITargettable, IPathFindingAgent, IProjectileCompatibleEntity





.. dn:class:: Clay.Game.Mod.Entities.Seed
    :hidden:

.. dn:class:: Clay.Game.Mod.Entities.Seed


Constructors
------------

.. dn:class:: Clay.Game.Mod.Entities.Seed
    :noindex:
    :hidden:

    .. dn:constructor:: Clay.Game.Mod.Entities.Seed.Seed()




        .. code-block:: csharp

            public Seed()



Properties
----------

.. dn:class:: Clay.Game.Mod.Entities.Seed
    :noindex:
    :hidden:

    .. dn:property:: Clay.Game.Mod.Entities.Seed.ProjectileToCreate



        :rtype: System.String

        .. code-block:: csharp

            public string ProjectileToCreate { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Seed._flora



        :rtype: System.String

        .. code-block:: csharp

            public string _flora { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Seed._freeBehaviour



        :rtype: System.String

        .. code-block:: csharp

            public string _freeBehaviour { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Seed._freeSpeed



        :rtype: System.Single

        .. code-block:: csharp

            public float _freeSpeed { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Seed._freeTargetBehaviour



        :rtype: System.String

        .. code-block:: csharp

            public string _freeTargetBehaviour { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Seed._fruitSprite



        :rtype: System.String

        .. code-block:: csharp

            public string _fruitSprite { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Seed._leafType



        :rtype: System.String

        .. code-block:: csharp

            public string _leafType { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Seed._projectile



        :rtype: System.String

        .. code-block:: csharp

            public string _projectile { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Seed._sourceLeafTypes



        :rtype: System.String<System.String>[]

        .. code-block:: csharp

            public string[] _sourceLeafTypes { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Seed.isTargetable



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool isTargetable { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Seed.isTranscendenceCompatible



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isTranscendenceCompatible { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Seed.projectile



        :rtype: SeedProjectile

        .. code-block:: csharp

            public SeedProjectile projectile { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Seed.spawnHeader



        :rtype: System.String

        .. code-block:: csharp

            public override string spawnHeader { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Seed.useSpawnEntityCommand



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool useSpawnEntityCommand { get; }



Methods
-------

.. dn:class:: Clay.Game.Mod.Entities.Seed
    :noindex:
    :hidden:

    .. dn:method:: Clay.Game.Mod.Entities.Seed.CloneConfiguration(Tuna.Mob)



        :type mob: Tuna.Mob


        .. code-block:: csharp

            public override void CloneConfiguration(Mob mob)

    .. dn:method:: Clay.Game.Mod.Entities.Seed.Deactivate(System.Boolean)



        :type quietly: System.Boolean

        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool Deactivate(bool quietly)

    .. dn:method:: Clay.Game.Mod.Entities.Seed.FreeEnterState(System.Boolean)



        :type quietly: System.Boolean


        .. code-block:: csharp

            public void FreeEnterState(bool quietly)

    .. dn:method:: Clay.Game.Mod.Entities.Seed.InitialiseApp()




        .. code-block:: csharp

            public static void InitialiseApp()

    .. dn:method:: Clay.Game.Mod.Entities.Seed.InitialiseLevel()




        .. code-block:: csharp

            public static void InitialiseLevel()

    .. dn:method:: Clay.Game.Mod.Entities.Seed.ParentColonised()




        .. code-block:: csharp

            public override void ParentColonised()

    .. dn:method:: Clay.Game.Mod.Entities.Seed.SpawnRandom(UnityEngine.Vector2)



        :type position: UnityEngine.Vector2

        :rtype: Clay.Game.Mod.Entities.Seed

        .. code-block:: csharp

            public static Seed SpawnRandom(Vector2 position)

    .. dn:method:: Clay.Game.Mod.Entities.Seed.SpawnSeed(System.String[])



        :type parameters: System.String<System.String>[]

        :rtype: Clay.Game.Mod.Entities.Seed

        .. code-block:: csharp

            public static Seed SpawnSeed(string[] parameters)

    .. dn:method:: Clay.Game.Mod.Entities.Seed.SpawnSeedLua(System.String)



        :type parameters: System.String

        :rtype: Clay.Game.Mod.Entities.Seed

        .. code-block:: csharp

            public static Seed SpawnSeedLua(string parameters)

    .. dn:method:: Clay.Game.Mod.Entities.Seed.Trashed()




        .. code-block:: csharp

            public override void Trashed()

    .. dn:method:: Clay.Game.Mod.Entities.Seed.Update(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public override void Update(float time)



